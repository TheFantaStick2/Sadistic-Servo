import RPi.GPIO as GPIO
import time

verticalPIN = 17
horizonPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(verticalPIN, GPIO.OUT)
GPIO.setup(horizonPIN, GPIO.OUT)


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

print
print("This is the interactive experimental 2-Achsis-Platform-Remote-Control-Script using SRU for your convinience.")
print("If you need help, just ask for it!")
print

#platform system process
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
	 
command = raw_input("?")

#expecting input
while command != "exit":
	if command == "turnh":
		try:
			hs = ht  #saving the current value of ht
			ht = float(raw_input("set turn horizontally: "))
			if 2.5 <= ht <= 10:
				h.ChangeDutyCycle(ht)
				time.sleep(0.5)
				h.ChangeDutyCycle(0)
				command = raw_input("?")
			else:
				ht = hs  #resetting ht to saved value
				print("Please enter a number between 2.5 and 10!")
				command = raw_input("?")
		except ValueError:  #if input is not a float, programm will not crash
			print ("You now what numbers are, right?")
			command = raw_input("?")

        elif command == "turnv":
                try:
                        vs = vt
                        vt = float(raw_input("set turn vertically: "))
                        if 2.5 <= vt <= 10:
                                v.ChangeDutyCycle(vt)
                                time.sleep(0.5)
                                v.ChangeDutyCycle(0)
                                command = raw_input("?")
                        else:
                                vt = vs
                                print("Please enter a number between 2.5 and 10!")
                                command = raw_input("?")
                except ValueError:  #if input is not a float, programm will not crash
                        print ("You now what numbers are, right?")
                        command = raw_input("?")

	elif command == "up":
		if vt + 0.5 != 10.5:
			vt = vt + 0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			v.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("There is no space to go up!")
			command = raw_input

	elif command == "down":
		if vt - 0.5 != 2:
			vt = vt - 0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			h.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("You can't go down even more!")
			command = raw_input("?")

	elif command == "left":
		if ht + 0.5 != 10.5:
			ht = ht + 0.5
			h.ChangeDutyCycle(ht)
			time.sleep(0.5)
			h.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("One more to the left and you would meet Lenin!")
			command = raw_input("?")

	elif command == "right":
		if ht - 0.5 != 2:
			ht = ht - 0.5
			h.ChangeDutyCycle(ht)
			time.sleep(0.5)
			h.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("You would turn brown. Aborting requested movements.")
			command = raw_input("?")

	elif command == "status":
		print
		print("Your current verticall position is: ")
		print(vt)
		print("Your current horizontal position is: ")
		print(ht)
		command = raw_input("?")

	elif command == "stop":
		v.stop()
		h.stop()
		command = raw_input ("?")

	elif command == "help":
		help()
		command = raw_input ("?")

	else:
		print("Fuck you, learn how to write")
		command = raw_input("?")
                
v.stop()
h.stop()

GPIO.cleanup()
print("[Done]")
