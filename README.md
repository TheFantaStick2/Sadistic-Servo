# Sadistic-Dual-Servo
Operate under your own risk.
The creator of this repository is NOT responsible for ANY harm or damage that might have been caused by using it.


Operate two servos.

I used this Script in order to turn a mounted webcam on two achsis. 


!! Still a Work in Progress. !!
>>I still need to fix the positioning :)



Instructions for use as 2-achsis-platform
----------------------------------------------------------------------------

Wire the signal of the servo, responsible for vertical turning to Pin 11 (GPIO 17) on a Raspberry Pi B+ v1.2.
Wire the signal of the horizontal servo to Pin 13 (GPIO 27).

I used an external energy source and wired the black to minus and red to plus, providing both servos with 6Volt.

----------------------------------------------------------------------------

server.py and client.py are intendet to be used for remote control using sockets and pygame for simple keystroke input.
therefore run the server.py on your rpi and the client.py on the control-computing unit. You will be asked which IP to use,
the programm will by default use port 4242.
please keep in mind, that this is still a work in progress and by no means a professional work.


Made by Piet.
