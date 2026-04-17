from flask import Flask, request, jsonify
from utils.video_generator import VideoGenerator

app = Flask(__name__)
video_generator = VideoGenerator()

@app.route('/upload_ecg', methods=['POST'])
def upload_ecg():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    ecg_data = file.read()
    video_path = video_generator.generate_video(ecg_data)

    return jsonify({'video_path': video_path}), 200

if __name__ == '__main__':
    app.run(debug=True)