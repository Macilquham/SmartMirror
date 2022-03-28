
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 64
rawCapture = PiRGBArray(camera, size=(640, 480))

img = cv2.imread("sunglasses.png",cv2.IMREAD_UNCHANGED)
# cv2.imshow("Frame", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
     image = frame.array
     cv2.imshow("Frame", image)
     key = cv2.waitKey(1) & 0xFF
     rawCapture.truncate(0)