#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB

# Drive the motor clockwise
# Motor A:
GPIO.output(12, GPIO.HIGH) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
# Motor B:
GPIO.output(15, GPIO.HIGH) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
# Motor A:
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.HIGH) # Set AIN2
# Motor B:
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.HIGH) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(13, GPIO.LOW) # Set STBY
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB
#from gpiozero import Motor
#from gpiozero import Robot

#robby = Robot(left=(7,8), right=(9,10))
#robby.forward()

#motor1 = Motor(4, 14)
#motor2 = Motor(17, 27)

# motor1.forward()
# motor2.backward()


#motor1.forward(0.5)
#motor2.backward(0.5)

# motor1.forward()
# motor2.backward()
# while True:
    # sleep(5)
 #   motor1.reverse()
 #   motor2.reverse()
    
#motor1.stop()
#motor2.stop()
