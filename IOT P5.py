from picamera import PiCamera
from time import sleep
import datetime

# Create a PiCamera object
camera = PiCamera()

# Start the camera preview
camera.start_preview()

# Get the current date and time
current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Wait for a few seconds before capturing to allow the camera to adjust
sleep(3)

# Capture an image and save it with the current date and time as the filename
camera.capture('/home/pi/Desktop/MCASyllabus/images/{}.jpg'.format(current_date))

# Stop the camera preview
camera.stop_preview()

# Print a message indicating that the image has been captured
print("Image captured")
