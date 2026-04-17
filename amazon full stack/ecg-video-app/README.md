# ECG Video Application

This project is a web application that generates videos from ECG (Electrocardiogram) signals. It consists of a backend built with Flask and a frontend that allows users to interact with the application.

## Project Structure

```
ecg-video-app
├── backend
│   ├── app.py                # Main entry point for the backend application
│   ├── requirements.txt      # Python dependencies for the backend
│   └── utils
│       └── video_generator.py # Contains the VideoGenerator class for video creation
├── frontend
│   ├── index.html            # Main HTML file for the frontend
│   ├── script.js             # JavaScript for handling user interactions
│   └── style.css             # CSS for styling the frontend
└── README.md                 # Documentation for the project
```

## Backend

### Setup

1. Navigate to the `backend` directory.
2. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

### Running the Application

To start the Flask server, run the following command:

```
python app.py
```

The server will start and listen for incoming requests.

### API Endpoints

- **POST /upload**: Upload ECG data for video generation.
- **GET /video**: Retrieve the generated video.

## Frontend

### Setup

1. Open `index.html` in a web browser to access the application.

### Usage

- Use the provided interface to upload ECG data.
- The application will process the data and generate a video representation.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.