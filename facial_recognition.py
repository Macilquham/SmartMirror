# TechVidvan Face detection

import cv2
import face_recognition
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import RPi.GPIO as GPIO
from gui import SmartMirror
from facial_recognition_data_capture import FacialRecognitionDataCapture

encodedFaces = FacialRecognitionDataCapture().EncodedImages()
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 64
rawCapture = PiRGBArray(camera, size=(640, 480))
print("Ready")

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array
    Current_image = cv2.resize(img,(0,0),None,0.25,0.25)
    Current_image = cv2.cvtColor(Current_image, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(Current_image, model='hog')  
    face_encodes = face_recognition.face_encodings(Current_image,face_locations)

    for encodeFace,faceLocation in zip(face_encodes,face_locations):
        matches = face_recognition.compare_faces(encodedFaces,encodeFace, tolerance=0.6)

        if any(matches):
            index = [index for index, item in enumerate(matches) if item][0]
            smartMirror = SmartMirror()
            smartMirror.execute()

    key = cv2.waitKey(1)        
    rawCapture.truncate(0)