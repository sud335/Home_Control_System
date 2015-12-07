import RPi.GPIO as gp
import sys,time
import json
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(21,gp.OUT)

dicti = {"green":7,"yellow":11,"red":21}
option = {1:"green",2:"yellow",3:"red"}


print ""

def twoLeds(light1,light2):

    gp.output(dicti[option[light1]],True)
    gp.output(dicti[option[light2]],True)


def threeLeds():

    for key in dicti.keys():

        gp.output(dicti[key],True)
        

def oneLed(light):
    gp.output(dicti[option[light]],True)

def wave():
    import time
    keys=["green","yellow","red"]
    flag =0
    while flag==0:
        for key in keys:
            
            gp.output(dicti[key],True)
	    if not gp.input(dicti[key]):
		flag=1
            time.sleep(1)
            gp.output(dicti[key],False)

def callFunc():
    option=0
    while option<5 :
        print ""
        print "1 - One Led    2 - Two Leds   3 - Three Leds    4 - Wave    5 - Quit" 
        print ""

        option = raw_input("Enter your choice : ")
        option = int(option)

        if option == 1:
            print ""
            light = raw_input("Enter your number for led :")
            oneLed(int(light))

        elif option == 2:
            print ""
            light1 = raw_input("Enter your number for led1 :")
            print ""
            light2 = raw_input("Enter your number for led2 :")
            while light2 == light1:
                print "Sorry the numbers cannot be same : "
                light2 = raw_input("Enter your number for led2 :")
            twoLeds(int(light1),int(light2))

        elif option ==3:
            threeLeds()

        elif option==4:
            wave()

        else:
            print "Bye!! "
            break

def mainCall(get_input):
	key = get_input.keys()[0]
	if key == "wave":
		wave()
	elif key == "three":
		threeLeds()
	elif key == "two":
		lis=get_input[key]
		twoLeds(int(lis[0]),int(lis[1]))
	elif key == "one":
		lis=get_input[key]
		oneLed(int(lis[0]))
args=sys.argv
import os
mainCall(eval(args[1]))
print json.dumps({"status":"1"})    

    


    
