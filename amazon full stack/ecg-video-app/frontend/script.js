const uploadButton = document.getElementById('upload-button');
const videoContainer = document.getElementById('video-container');

uploadButton.addEventListener('change', handleFileUpload);

function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('ecgFile', file);

        fetch('/api/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.videoUrl) {
                displayVideo(data.videoUrl);
            } else {
                alert('Error generating video');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while uploading the file');
        });
    }
}

function displayVideo(videoUrl) {
    const videoElement = document.createElement('video');
    videoElement.src = videoUrl;
    videoElement.controls = true;
    videoElement.autoplay = true;
    videoContainer.innerHTML = ''; // Clear previous video
    videoContainer.appendChild(videoElement);
}