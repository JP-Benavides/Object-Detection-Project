import cv2
import numpy as np
import tempfile
from PIL import Image as img

def save_temp_image(pil_image):
    with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as tempfile:
        temp
    
#Capture Video
video_path = 'example.mp4'
capture = cv2.VideoCapture(video_path)

#Checks if video opens 
if not capture.isOpened():
    print("Video cannot be openned")
    exit()


#Set Custom Frame
num_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
custom_frame = input(f"What frame would you like to train from from 1 to {num_frames}")
capture.set(cv2.CAP_PROP_POS_FRAMES, custom_frame)
ret, frame = capture.read()
if not ret: 
    print("Could not read frame")
    exit()



#Custom Frame to file

while capture.isOpened():
    
    ret, frame = capture.read()

    if not ret: 
        print("Cant recieve frame...exiting")
        break 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)

    #Press q to terminate 
    if cv2.waitKey(1) == ord('q'):
        break