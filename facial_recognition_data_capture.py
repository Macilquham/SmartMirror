
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import face_recognition
import pickle
from os import listdir
from os.path import exists
import numpy as np

class FacialRecognitionDataCapture:
    
    def CaptureTrainingImages(self):
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 64
        rawCapture = PiRGBArray(camera, size=(640, 480))

        count = 0
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) 
            if key == ord('c'):
                cv2.imwrite(f'./Faces/face{count}.jpg',image)
                count = count + 1
                
            rawCapture.truncate(0)

    def EncodedImages(self):
        path_to_file ='dataset_faces.dat'
        if exists(path_to_file):
            with open(path_to_file, 'rb') as f:
                all_face_encodings = pickle.load(f)
                return  np.array(list(all_face_encodings))
        else:
            encoded_images = self.EncodeImages()
            with open(path_to_file, 'wb') as f:
                    pickle.dump(encoded_images, f)

            return encoded_images


    def EncodeImages(self):
        path = 'Faces'
        images = []
        for img in listdir(path):
            image = cv2.imread(f'{path}/{img}')
            images.append(image)
            # classNames.append(str.split(img,".")[0])

        encodeList = []
        for img in images[0:2]:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            print(encode)
            encodeList.append(encode)

        
        return encodeList


if __name__ == "__main__":
    FacialRecognitionDataCapture().CaptureTrainingImages()