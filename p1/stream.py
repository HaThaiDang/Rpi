import cv2
from flask import Flask, Response

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)  # 0 for the default camera, change to the desired camera if needed

def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
