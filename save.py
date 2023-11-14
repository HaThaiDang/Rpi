import cv2
import socket
import pickle
import struct

def receive_and_save_video():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('169.254.153.172', PORT))
    server_socket.listen(5)

    conn, addr = server_socket.accept()
    data = b""
    payload_size = struct.calcsize("Q")

    frames = []

    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += conn.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        frames.append(frame)
        cv2.imshow('Video from Raspberry Pi', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Save received frames as a video file
    video_writer = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (640, 480))
    
    for frame in frames:
        video_writer.write(frame)

    video_writer.release()

    cv2.destroyAllWindows()

# Receive video frames and save the video
receive_and_save_video()
