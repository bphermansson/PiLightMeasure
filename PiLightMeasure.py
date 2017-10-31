#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

# Modified by Patrik Hermansson 160526
__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"

GPIO.setmode(GPIO.BOARD)
if len(sys.argv) <= 1:
	print "Command error, give arguments \"c\" (continous) or \"o\" (one time)"  
	sys.exit(0)
else:
	arg = sys.argv[1]

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    # Load the capacitor
    GPIO.output(pin_to_circuit, GPIO.HIGH)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes low
    while (GPIO.input(pin_to_circuit) == GPIO.HIGH):
        count += 1

    return count

#Caltch when script is interupted, cleanup correctly
try:
    # Main loop
    prints "Rpi light measure"
    if arg == "o":
	# One measurent only
	print rc_time(pin_to_circuit)
    elif arg == "c":
	# Continous measures
        while True:
		print rc_time(pin_to_circuit)
    else: 
	print "Command error, give arguments \"c\" (continous) or \"o\" (one time)"  
	sys.exit(0)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
