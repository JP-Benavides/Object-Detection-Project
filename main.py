import cv2
import numpy as np
import tempfile
from PIL import Image as img
from labelImg import labelImg as label
import subprocess as sp

def open_labelimg(temp_path):
    try: 
        command = f"labelImg {temp_path}"
        sp.run(command, check = True)
        print("Labelimg is opening")

    except sp.CalledProcessError as e:
        print("An error has occured, cannot open labelImg:",e)

def check_readability(ret):
    if not ret: 
        print("Could not read frame")
        exit()
    else: 
        print("Frame is read")

def save_temp_image(pil_image):
    with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as tp:
        temp_file_path = tp.name
        pil_image.save(temp_file_path)
        print(f"Image was saved temporairily at {temp_file_path}")
        tp.flush()
        return temp_file_path
    
#Capture Video
video_path = "C:/Users/JP/Downloads/12267384_3840_2160_30fps.mp4"
capture = cv2.VideoCapture(video_path)

#Checks if video opens 
if not capture.isOpened():
    print("Video cannot be openned")
    exit()

#Set Custom Frame
num_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
custom_frame = int(input(f"What frame would you like to train from from 1 to {num_frames}"))
capture.set(cv2.CAP_PROP_POS_FRAMES, custom_frame)
ret, frame = capture.read()
check_readability(ret)

#Create Temp Image 
pil_image = img.fromarray(frame)
temp_path = save_temp_image(pil_image)

#Custom Frame to file
open_labelimg(temp_path)




'''
#Train YOLO through each frame 
while capture.isOpened():
    
    ret, frame = capture.read()

    check_readability(ret)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)


    #Press q to terminate
    print("Press q to terminate manually") 
    if cv2.waitKey(1) == ord('q'):
        break
'''