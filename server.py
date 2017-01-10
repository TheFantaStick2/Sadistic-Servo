import socket
import RPi.GPIO as GPIO
import time

print ("Please enter host IP")
host = raw_input ("?")
print
print ("The server will be launched on: "), host, (":4242")

print ("Setting up Sockets...")

s = socket.socket()
s.bind((host, 4242))
s.listen(5)

print ("  ...[DONE]")
print ("Setting up PINs...")

verticalPIN = 17
horizonPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(verticalPIN, GPIO.OUT)
GPIO.setup(horizonPIN, GPIO.OUT)

print ("  ...creating variables")

#setting GPIO 17&27 as PWM with 50Hz
#Initilization (Moving to default positioning)
v = GPIO.PWM(verticalPIN, 50)
v.start(2.5)
time.sleep(0.5)
v.ChangeDutyCycle(0)
vt = 2.5  #setting up vertical position variable

h = GPIO.PWM(horizonPIN, 50)
h.start(2.5)
time.sleep(0.5)
h.ChangeDutyCycle(0)
ht = 2.5

print ("  ...[DONE]")
print
print ("Waiting for client ...")

while 1:
	(clientsocket, address) = s.accept()
	print ("  ...Got connection from"), address
	clientsocket.send ("Connected to: "), host, (":4242")
	if clientsocket.recv == ("ld"):
		if ht+0.5 != 10.5:
			ht = ht+0.5
			h.ChangeDutyCycle(ht)
			time.sleep(0.5)
			h.ChangeDutyCycle(0)
	if clientsocket.recv == ("rd"):
		if ht-0.5 != 2:
			ht = ht-0.5
			h.ChangeDutyCycle(ht)
			time.sleep(0.5)
			h.ChangeDutyCycle(0)
	if clientsocket.recv == ("ud"):
		if vt+0.5 != 10.5:
			vt = vt+0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			v.ChangeDutyCycle(0)
	if clientsocket.recv == ("dd"):
		if vt-0.5 != 2:
			vt = vt-0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0)
			v.ChangeDutyCycle(0)
	if  clientsocket.recv == ("s"):
		v.stop()
		h.stop()

clientsocket.close()
