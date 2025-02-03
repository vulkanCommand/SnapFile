// S3 Bucket Details
const bucketName = 'user-file-storage-app'; // Replace with your bucket name
const region = 'us-east-1'; // Replace with your bucket's region
const bucketUrl = `https://${bucketName}.s3.${region}.amazonaws.com`;

// Function to List Files from S3
function listFiles() {
    const fileListElement = document.getElementById('file-list');

    // Public URL to list files
    fetch(`${bucketUrl}?list-type=2`)
        .then(response => response.text())
        .then(data => {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(data, 'text/xml');
            const contents = xmlDoc.getElementsByTagName('Contents');

            // Clear existing list
            fileListElement.innerHTML = '';

            // Loop through files
            for (let i = 0; i < contents.length; i++) {
                const fileName = contents[i].getElementsByTagName('Key')[0].textContent;

                // Create list item
                const listItem = document.createElement('li');
                listItem.innerHTML = `
                    ${fileName} - 
                    <a href="${bucketUrl}/${fileName}" target="_blank">Download</a>
                `;
                fileListElement.appendChild(listItem);
            }
        })
        .catch(error => console.error('Error fetching files:', error));
}

// Run the function on page load
document.addEventListener('DOMContentLoaded', listFiles);
