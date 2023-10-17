import cv2
import numpy as np
import requests

url = 'http://COMPUTER1_IP:5000/video'  # Replace COMPUTER1_IP with Computer 1's IP address

cap = cv2.VideoCapture(url)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('received_video.avi', fourcc, 20.0, (640, 480))  # Adjust resolution and framerate as needed

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('Received Video', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
