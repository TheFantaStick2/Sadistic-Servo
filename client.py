import time
import socket
import pygame
import pygame.key
from pygame.locals import *

print ("Please enter target IP:")
host = raw_input ("?")
print

s = socket.socket()
s.connect((host, 4242))
print s.recv (2048)

#platform system processes
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
camkeys=[False,False,False,False]

main_loop = 1

while main_loop:
	pygame.display.set_caption("Sadistic-Dual-Servo-Control")
	screen.fill(0)

	if camkeys[0] == True:
		s.send("ld")
		time.sleep(0.5)
	if camkeys[1] == True:
		s.send("rd")
		time.sleep(0.5)
	if camkeys[2] == True:
		s.send("ud")
		time.sleep(0.5)
	if camkeys[3] == True:
		s.send("dd")
		time.sleep(0.5)

	if camkeys[0]==False and camkeys[1]==False and camkeys[2]==False and camkeys[3]==False:
		s.send("s")
		

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_q:
				s.close
				pygame.quit()
				exit(0)

		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				camkeys[0]=True
			elif event.key == K_RIGHT:
				camkeys[1]=True
			elif event.key == K_UP:
				camkeys[2]=True
			elif event.key == K_DOWN:
				camkeys[3]=True

		if event.type == pygame.KEYUP:
			if event.key == K_LEFT:
				camkeys[0]=False
			elif event.key == K_RIGHT:
				camkeys[1]=False
			elif event.key == K_UP:
				camkeys[2]=False
			elif event.key == K_DOWN:
				camkeys[3]=False

