import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0) 

signal.signal(signal.SIGINT, signal_handler)

power_pin = 19
reverse_pin = [26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(power_pin, GPIO.OUT)
# GPIO.output(power_pin, 0)

GPIO.setup(reverse_pin, GPIO.OUT)
GPIO.output(reverse_pin, 0)

p = GPIO.PWM(power_pin, 300); # 1000 Hz
p.start(0);

def unlockLock(): 
    lockDoor();
    sleep(1.3);
    unlockDoor();
def lockDoor():
    p.ChangeDutyCycle(30.0);
    #GPIO.output(power_pin, 1);
    GPIO.output(reverse_pin, 1);
    sleep(0.2);
    p.ChangeDutyCycle(0);
    #GPIO.output(power_pin, 0);
    GPIO.output(reverse_pin, 0);

def unlockDoor(): 
    
    p.ChangeDutyCycle(30.0);
    #GPIO.output(power_pin, 1);
    #GPIO.output(power_pin, 1);
    GPIO.output(reverse_pin, 0);
    sleep(0.2);
    p.ChangeDutyCycle(0);
    #GPIO.output(power_pin, 0);

with open('labels', 'rb') as f:
        dicti = pickle.load(f)
        f.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 3
rawCapture = PiRGBArray(camera, size=(640, 480))


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

font = cv2.FONT_HERSHEY_SIMPLEX

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame = frame.array
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
        print("new frame")
        for (x, y, w, h) in faces:
                roiGray = gray[y:y+h, x:x+w]

                id_, conf = recognizer.predict(roiGray)

                for name, value in dicti.items():
                        if value == id_:
                                print(name)

                print(conf);
                if conf >= 70:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)
                        unlockLock();
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        rawCapture.truncate(0)

        if key == 27:
                break

cv2.destroyAllWindows()
