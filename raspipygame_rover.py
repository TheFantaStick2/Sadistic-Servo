import time
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

print("Setting up GPIOs ...")

GPIO.setwarnings(False)

leftPIN = 17
rightPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftPIN, GPIO.OUT)
GPIO.setup(rightPIN, GPIO.OUT)
print("  ...Assigned PINs")

#setting GPIO17 & GPIO27 as PWM with 100Hz
#Initilization (Giving the ESC a signal)
l = GPIO.PWM(leftPIN, 100)
l.start(10)
time.sleep(0.5)

r = GPIO.PWM(rightPIN, 100)
r.start(10)
time.sleep(0.5)

print("  ...Assigned variables")

#setting up speed variables
rs = 5
rs = 5
print("  ...Created position variables")
print("  ...[Done]")

#platform system processes
print("Defining functions ...")
def help():
	print
	print("Commands:")
	print
	print("========================================================")
	print
	print("SRU			SomeRandomUnit")
	print
	print("turnv			Enter specific vertical position")
	print("turnh			Enter specific horizontal position")
	print
	print("up			Raises 0.5SRU up")
	print("down			Raises 0.5SRU down")
	print("left			Turns 0.5SRU left")
	print("right			Turns 0.5SRU right")
	print
	print("status			Prints the current positions")
	print("stop			Halt all movements")
	print("help			That's how you got here")
	print("exit			Stopping all movements s but remaining in position")
	print
	print("========================================================")
	print
	print("Script created by Piet.")
	print
	return 0

#starting pygame and setting up display window
pygame.init()
screen = pygame.display.set_mode((480, 500))

#creating boolean list for arrow keys
roverkeys=[False,False,False,False]

main_loop = 1

while main_loop:
	pygame.display.set_caption("Rover-Local-Control")
	screen.fill(0)

	#Defining steering
	if roverkeys[0] == True:
		l.ChangeDutyCycle(12.5)
		r.ChangeDutyCycle()
	if roverkeys[1] == True:
		l.ChangeDutyCycle()
		r.ChangeDutyCycle(12.5)
	if roverkeys[2] == True:
		l.ChangeDutyCycle(12.5)
		r.ChangeDutyCycle(12.5)
	if roverkeys[3] == True:
		l.ChangeDutyCycle(10)
		r.ChangeDutyCycle(10)

	if roverkeys[0]==False and roverkeys[1]==False and roverkeys[2]==False and roverkeys[3]==False:
		l.stop(10)
		r.stop(10)
		

	for event in pygame.event.get():
		if event.type == pygame.Quit:
			pygame.quit()
			exit(0)

		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				roverkeys[0]=True
			elif event.key == K_Right:
				roverkeys[1]=True
			elif event.key == K_UP:
				roverkeys[2]=True
			elif event.key == K_DOWN:
				roverkeys[3]=True

		if event.type == pygame.KEYUP:
			if event.key == K_LEFT:
				roverkeys[0]=False
			elif event.key == K_RIGHT:
				roverkeys[1]=False
			elif event.key == K_UP:
				roverkeys[2]=False
			elif event.key == K_DOWN:
				roverkeys[3]=False

