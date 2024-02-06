import cv2
from flask import Flask, render_template, Response
import threading
import time
from datetime import datetime

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

# Set camera resolution to 1920x1080
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# Function to capture images and save them with timestamp in the current folder
def capture_images():
    while True:
        _, frame = video_capture.read()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"image_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        time.sleep(5)  # Capture an image every 5 seconds

# Start the image capture thread
image_thread = threading.Thread(target=capture_images)
image_thread.daemon = True
image_thread.start()

# Function to generate frames for the Flask web page
def generate_frames():
    while True:
        with open("current_image.jpg", "rb") as f:
            frame = f.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        time.sleep(0.1)

# Route to render the HTML page with the image
@app.route('/')
def index():
    return render_template('index.html')

# Route for streaming video
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
