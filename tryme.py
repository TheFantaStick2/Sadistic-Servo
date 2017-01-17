# I have nothing to test this on, but it might work ;)
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
s.listen(10)

print ("  ...[DONE]")
print ("Setting up PINs...")

GPIO.setwarnings(False)
leftPIN = 17
rightPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftPIN, GPIO.OUT)
GPIO.setup(rightPIN, GPIO.OUT)

print ("  ...creating variables")

#setting GPIO 17&27 as PWM with 100Hz
#Initilization (Moving to default positioning)
l = GPIO.PWM(leftPIN, 100)
l.start(10)

r = GPIO.PWM(rightPIN, 100)
r.start(10)
speed = 10

print ("  ...[DONE]")
print
print ("Waiting for client ...")

x = 1


while x == 1:
	(clientsocket, address) = s.accept()
	print ("  ...Got connection from"), address
	clientsocket.send ("Connected to: "), host, (":4242")
	candy = clientsocket.recv(4096)
	if candy == ("ld"):  #turning
			l.ChangeDutyCycle(20)
			r.ChangeDutyCycle(7.5)
	if candy == ("rd"):
			l.ChangeDutyCycle(7.5)
			r.ChangeDutyCycle(20)
	if clandy == ("ud"):  #speedcontrol
		if speed+2.5 != 22.5:
			speed = speed+2.5
			l.ChangeDutyCycle(speed)
			r.ChangeDutyCycle(speed)
		else:
			clientsocket.send ("tf")
	if candy == ("dd"):
		if speed-2.5 != 7.5:
			speed = speed-2.5
			l.ChangeDutyCycle(speed)
			r.ChangeDutyCycle(speed)
		else:
			clientsocket.send ("ts")
	#if  clientsocket.recv == ("s"):
	#	r.ChangeDutyCycle(7.5)
	if candy == ("b"):  #halting
		l.ChangeDutyCycle(10)
		r.ChangeDutyCycle(10)
	if candy == ("q"):
		x = 2
clientsocket.close()
