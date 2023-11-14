import cv2
import time

def start_video_stream():
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera (usually the built-in webcam)
    return cap

def save_video(cap, output_filename, duration):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame")
            break
        out.write(frame)
        cv2.imshow('Video Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_stream = start_video_stream()
    
    # Set the filename for saving the video
    filename = "output_video.avi"

    # Set the duration for each video recording in seconds
    recording_duration = 10

    try:
        while True:
            save_video(video_stream, filename, recording_duration)
    except KeyboardInterrupt:
        print("Recording stopped by user")

