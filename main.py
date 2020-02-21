#!/usr/bin/python

'''
	Author: ILGIN DOĞAN -- lgndogan@gmail.com
	A Simple Motion Detection v1.0
'''
# You need to install picamera to run this script
import motionDetecting
import picamera
from time import sleep
from datetime import date,datetime
import time

motionState = False
path = "/home/pi/Desktop/images" #Raspberry pi folder directory
# path = "your directory saving image "
while True:
	dateStringPhoto = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
	motionState = motionDetecting.motion() # Using Motion function from motionDetecting
	print(motionState) # Status of Motion True or False
	if motionState:
		print("Motion Detected")
		with picamera.PiCamera() as camera:
			# This Camera Configuration is based on NoIR Picamera, you can change your PiCamera Version.
			camera.resolution = (1280,720)
            camera.shutter_speed = (20000)
            camera.exposure_mode = "night"
            camera.awb_mode = "sunlight"
			camera.capture(path+"/motion"+dateStringPhoto+".jpg") # İmage name restore the time
			camera.close()
		print("Saved İmage According to Motion")
