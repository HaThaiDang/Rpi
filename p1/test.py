import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it to 1, 2, etc. for different cameras)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Display the frame
    cv2.imshow('Camera Stream', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
