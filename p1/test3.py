import cv2
from flask import Flask, Response

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)  # 0 for the default camera, change to the desired camera if needed

# Define the codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # You can customize the filename, codec, frame rate, and resolution

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
            out.write(frame)  # Write the frame to the VideoWriter object to save the video
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# Release the VideoWriter object and release the camera when the program exits
out.release()
video_capture.release()
cv2.destroyAllWindows()
