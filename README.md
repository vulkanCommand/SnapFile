# SnapFile - Automated File Sync to AWS S3

## Overview
SnapFile is an automated file synchronization system that detects changes in a local folder and seamlessly uploads new or modified files to an AWS S3 bucket. It also provides a simple web interface hosted on AWS S3, where users can view and download uploaded files in real time.

## Features
- **Automated File Uploads**: Detects new or modified files in the designated folder and uploads them to an S3 bucket.
- **Hosted Web Interface**: Displays uploaded files via an AWS S3-hosted website.
- **Task Scheduler Integration**: Runs automatically on system startup using Windows Task Scheduler.
- **Real-Time File Listing**: Webpage dynamically lists available files in the S3 bucket.

## Technologies Used
- **Python** (for file monitoring and uploading via `boto3`)
- **JavaScript** (to fetch and display file listings from S3)
- **AWS S3** (for file storage and website hosting)
- **HTML & CSS** (for the web interface)
- **Watchdog** (Python library for monitoring file changes)

## How It Works
1. **Monitor Folder Changes**
   - The `upload_monitor.py` script runs in the background and listens for file changes in the `SnapFile` directory.
2. **Upload to S3**
   - When a file is added or modified, the script uploads it to the configured AWS S3 bucket.
3. **Display on Webpage**
   - The hosted web interface retrieves the file list from the S3 bucket and displays them for users to access and download.
4. **Task Scheduler Automation**
   - The script is configured to start automatically on system boot using Windows Task Scheduler.

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SnapFile.git
cd SnapFile
```

### 2. Configure AWS Credentials
Edit `upload_monitor.py` with your AWS S3 credentials and bucket name.

### 3. Install Dependencies
```bash
pip install boto3 watchdog
```

### 4. Start the Monitor Script
```bash
python upload_monitor.py
```

### 5. Deploy Web Interface
1. Upload `index.html`, `script.js`, and `style.css` to your AWS S3 bucket.
2. Enable static website hosting in the S3 settings.

### 6. Automate with Task Scheduler (Windows)
1. Open Task Scheduler and create a new task.
2. Set the trigger to start at login.
3. Set the action to run `python upload_monitor.py`.

## Screenshots
![Screenshot 2025-02-03 134608](https://github.com/user-attachments/assets/8307af9b-a4b7-486b-90a0-26e134482fcd)
![Screenshot 2025-02-03 135034](https://github.com/user-attachments/assets/6fb25403-8119-49e5-a127-743e67fe475a)
![Screenshot 2025-02-03 135024](https://github.com/user-attachments/assets/f4da3225-313c-4c5e-803d-bd0e83a2abfc)
![Screenshot 2025-02-03 135003](https://github.com/user-attachments/assets/3b378545-33d1-4261-8355-8322ee64fc57)
![Screenshot 2025-02-03 134952](https://github.com/user-attachments/assets/00232f99-736f-4e1f-a678-e1ed7ec1d1d4)
![Screenshot 2025-02-03 134836](https://github.com/user-attachments/assets/3b0181cb-9b4f-445c-9598-f1b3163204b5)
![Screenshot 2025-02-03 134754](https://github.com/user-attachments/assets/bac29e7d-4ca6-4a20-b374-1c0c15ab7e72)
![Screenshot 2025-02-03 134652](https://github.com/user-attachments/assets/eaf4d57a-7823-44c6-a9d2-04dd9790d9a7)
![Screenshot 2025-02-03 134630](https://github.com/user-attachments/assets/9211b9d7-f5fc-4889-96da-d96ae5a116ec)
![Screenshot 2025-02-03 135303](https://github.com/user-attachments/assets/28e264bb-7294-44fa-9024-d40ea4a7d80b)


## Future Enhancements
- Implement user authentication for secure file access.
- Add support for multiple folders and buckets.
- Develop a desktop GUI for easier configuration.

## Contributing
Pull requests are welcome! Feel free to open an issue if you find a bug or have a feature request.

## License
MIT License. See `LICENSE` file for details.

