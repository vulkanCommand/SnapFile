import boto3
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# AWS S3 configuration
AWS_ACCESS_KEY = 'AKIAWQUOZHHHRDJKS5HD'
AWS_SECRET_KEY = '7I+yT1kvFsBWLfNiQ6U6dDD/pU8kiIQxoIhRRAsK'
AWS_REGION = 'us-east-1'  # Example: 'us-east-1'
BUCKET_NAME = 'user-file-storage-app'

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

# Define the folder to monitor
FOLDER_TO_MONITOR = r'C:\Users\gdkal\OneDrive\Documents\SnapFile' 

class S3UploadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.upload_to_s3(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.upload_to_s3(event.src_path)

    def upload_to_s3(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            print(f"Uploading {file_name} to S3 bucket {BUCKET_NAME}...")
            s3_client.upload_file(file_path, BUCKET_NAME, file_name)
            print(f"Uploaded {file_name} successfully.")
        except Exception as e:
            print(f"Failed to upload {file_name}: {e}")

if __name__ == "__main__":
    # Initialize the Watchdog Observer
    event_handler = S3UploadHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_MONITOR, recursive=False)
    
    print(f"Monitoring folder: {FOLDER_TO_MONITOR}")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping observer...")
    observer.join()


