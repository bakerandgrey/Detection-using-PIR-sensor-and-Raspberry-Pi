import RPi.GPIO as GPIO
import time
import requests
from num2words import num2words
from subprocess import call
cmd_beg= 'espeak '
cmd_end= ' 2>/dev/null'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
x=time.strftime("%H")       #to obtain system time in hours.
y=int(x)
while True:
	i=GPIO.input(11)
	if i==0:                 #When output from motion sensor is LOW
		print ("No intruders")
		time.sleep(1)
	elif i==1:               #When output from motion sensor is HIGH
		print ("Intruder detected")
		if y<12:
			text="Good Morning Welcome to baker and grey"
			print (text)
		elif y>=12 and y<16:
			text="Good afternoon Welcome to baker and grey"
			print (text)
		elif y>=16 and y<20:
			text="Good Evening Welcome to baker and grey"
			print(text)
		text = text.replace(' ', '_')
		#Calls the Espeak TTS Engine to read aloud a Text
		call([cmd_beg+text+cmd_end], shell=True)
		requests.post("https://maker.ifttt.com/trigger/YOUR-EVENT-NAME/with/key/YOUR-SECRET-KEY") #replace YOUR-EVENT-NAME and YOUR-SECRET-KEY
		time.sleep(2)
