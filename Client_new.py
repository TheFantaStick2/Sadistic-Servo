import time
import socket
import pygame
import pygame.key
from pygame.locals import *

print ("Please enter target IP:")
hostvar = raw_input ("?")
print

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostvar, 4242))
print s.recv (2048)

speed = 0

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
roverkeys=[False,False,False,False]

main_loop = 1

while main_loop:
	pygame.display.set_caption("upSTREAM Camera control")
	screen.fill(0)

	#True
	if roverkeys[0] == True:
		l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		l.connect((hostvar, 4242))
		time.sleep(1)
		l.send("ld")
		time.sleep(1)
		l.close()
		time.sleep(0.5)
	if roverkeys[1] == True:
		r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		r.connect((hostvar, 4242))
		time.sleep(1)
		r.send("rd")
		time.sleep(1)
		r.close()
		time.sleep(0.5)
	if roverkeys[2] == True:
		u = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		u.connect((hostvar, 4242))
		time.sleep(1)
		u.send("ud")
		time.sleep(1)
		u.close()
		time.sleep(0.5)
	if roverkeys[3] == True:
		d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		d.connect((hostvar, 4242))
		time.sleep(1)
		d.send("dd")
		time.sleep(1)
		d.close()
		time.sleep(0.5)

	#if roverkeys[0]==False and roverkeys[1]==False and roverkeys[2]==False and roverkeys[3]==False:
	#	b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#	b.connect((hostvar, 4242))
	#	time.sleep(1)
	#	b.send("ld")
	#	time.sleep(1)
	#	b.close()
	#	time.sleep(0.5)

	for event in pygame.event.get():
		#menu
		if event.type == pygame.KEYUP:
			if event.key == K_ESCAPE:
				q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				q.connect((hostvar, 4242))
				time.sleep(1)
				q.send("q")
				q.close
				pygame.quit()
				exit(0)

		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				roverkeys[0]=True
			elif event.key == K_RIGHT:
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

