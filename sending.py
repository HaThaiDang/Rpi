import cv2
import socket
import pickle
import struct
import time

# Function to capture a fixed-length video
def capture_fixed_length_video(duration_seconds):
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    start_time = time.time()
    frames = []

    while (time.time() - start_time) < duration_seconds:
        ret, frame = cap.read()
        frames.append(frame)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return frames

# Function to send video frames to PC
def send_video_to_pc(frames):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('PC_IP_ADDRESS', PORT))

    for frame in frames:
        data = pickle.dumps(frame)
        client_socket.sendall(struct.pack("Q", len(data)) + data)

    client_socket.close()

# Capture a fixed-length video (e.g., 10 seconds)
video_frames = capture_fixed_length_video(10)

# Send video frames to PC
send_video_to_pc(video_frames)
