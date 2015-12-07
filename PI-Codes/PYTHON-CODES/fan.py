import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(21,gp.OUT)

def perform(operation):
	if operation == "on":
		gp.output(21,gp.HIGH)
	else :
		gp.output(21,gp.LOW)
		gp.cleanup()

import sys

arg = sys.argv[1]

perform(arg)
