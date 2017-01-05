import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(10) # Initialisierung (10= signal present, Motorstop)

print
print("This is the interactive experimental Rover-Remote-Control-Script using SRU for your convinience.")
print("If you need help, just ask for it!")
print

#rover system process
def help():
        print
        print("Commands:")
        print
        print("========================================================")
        print
        print("run                      Starts the motor with a set speed in SRU")
        print("                 SRU: pulsetime in SomeRandomUnit")
        print("stop                     Stops the motor")
        print("exit                     Exits the programm")
        print
        print("========================================================")
        print
        print("Script created by Andy and Piet.")
        print
        return 0

command = raw_input("?")

#expecting input
while command != "exit":
        if command == "run":
                try:
                        g = float(raw_input("set speed in ms: "))
                        p.ChangeDutyCycle(g)
                        command = raw_input("?")
                except ValueError:  #if input is not a float, programm will not crash
                        print ("You now what numbers are, right?")

        elif command == "stop":
                p.ChangeDutyCycle(7.5)  #Brake with TestESC
                command = raw_input ("?")

        elif command == "help":
                help()
                command = raw_input ("?")

        else:
                print("May honey be poured over you, learn how to write!")
                command = raw_input("?")

p.ChangeDutyCycle(10)
GPIO.cleanup()
print("[Done]")
