#!/usr/bin/python


print "Content-Type: text/html; charset=UTF-8"  
print ""                                        

import cgi
import cgitb; cgitb.enable() 
import MySQLdb
import re
import random
import subprocess

subprocess.Popen(['sudo','python','/home/pi/off.py'])
