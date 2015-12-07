#!/usr/bin/python


print "Content-Type: text/html; charset=UTF-8"  
print ""                                        
import subprocess
import cgi
import cgitb; cgitb.enable()  
import MySQLdb
import re
import random
form = cgi.FieldStorage()

keyword=form.getvalue("keyword","#123none123#").strip()

if keyword!="#123none123#":
        subprocess.Popen(["sudo","python","/home/pi/fan.py",keyword])
        print keyword




