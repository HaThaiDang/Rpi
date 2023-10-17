import picamera
import time

# Create a Picamera object
camera = picamera.PiCamera()

# Set the resolution of the camera (optional)
camera.resolution = (640, 480)  # Adjust to your preferred resolution

# Start the video preview
camera.start_preview()

try:
    while True:
        # Add a sleep to control the frame rate (optional)
        time.sleep(1)

except KeyboardInterrupt:
    # Exit the program gracefully on Ctrl+C
    pass

finally:
    # Stop the preview and release resources
    camera.stop_preview()
    camera.close()
