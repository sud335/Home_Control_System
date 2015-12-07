#!/usr/bin/python

print "Content-Type: application/json; charset=UTF-8" 
print ""                                     
import subprocess
import cgi
import cgitb; cgitb.enable() 
import MySQLdb
import re,os
import random
form = cgi.FieldStorage()

keyword=form.getvalue("keyword","#123123#").strip()
#print "hi"
if keyword!="#123none123#":
        subprocess.Popen(["sudo","python","/home/pi/temper.py",keyword])
        #print keyword
	os.system("sudo python /home/pi/temper.py")
	k = open("temp","r").read()

	print k



