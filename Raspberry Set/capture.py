import io
import time
import picamera
camera = picamera.PiCamera()
import time
while True:
    camera.capture("snapshot.jpg")
    print("Updated")
    time.sleep(10)
