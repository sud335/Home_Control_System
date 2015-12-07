import RPi.GPIO as GPIO
import time,json

def bin2dec(string_num):
    return str(int(string_num, 2))
def run():
	import time
	data = []

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(26,GPIO.OUT)
	GPIO.output(26,GPIO.HIGH)
	time.sleep(0.025)
	GPIO.output(26,GPIO.LOW)
	time.sleep(0.02)

	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	for i in range(0,500):
    		data.append(GPIO.input(26))

#print len(data)
#print data
	bit_count = 0
	tmp = 0
	count = 0
	HumidityBit = ""
	TemperatureBit = ""
	crc = ""

	try:
		while data[count] == 1:
			tmp = 1
			count = count + 1
		for i in range(0, 32):
			bit_count = 0

			while count<500 and data[count] == 0:
				tmp = 1
				count = count + 1

			while count<500 and data[count] == 1:
				bit_count = bit_count + 1
				count = count + 1
			if bit_count > 3:
				if i>=0 and i<8:
					HumidityBit = HumidityBit + "1"
				if i>=16 and i<24:
					TemperatureBit = TemperatureBit + "1"
			else:
				if i>=0 and i<8:
					HumidityBit = HumidityBit + "0"
				if i>=16 and i<24:
					TemperatureBit = TemperatureBit + "0"

	except Exception as x:
		#print x
		#print "ERR_RANGE"
		#exit(0)
		pass

	try:
		for i in range(0, 8):
			bit_count = 0

			while count<500 and data[count] == 0:
				tmp = 1
				count = count + 1

	
			while count < 500 and data[count] == 1:
				bit_count = bit_count + 1
				count = count + 1

			if bit_count > 3:
				crc = crc + "1"
			else:
				crc = crc + "0"
	except Exception as x:
	#print x
	#print count , len(data)
	#print "ERR_RANGE1"
	#exit(0)
		pass
	import time
#Humidity = bin2dec(HumidityBit)
#Temperature = bin2dec(TemperatureBit)
	Humidity = bin2dec(HumidityBit)
	Temperature = bin2dec(TemperatureBit)


	if int(Humidity) + int(Temperature) - int(bin2dec(crc)) == 0:
		k= json.dumps({"Humidity":Humidity,"Temp": Temperature})
		open("/usr/lib/cgi-bin/temp","w").write(k)

		return 0
	else:
		if (int(Temperature)<=40 and int(Temperature)>=20 and int(Humidity)<=80):
			k=json.dumps({"Humidity":Humidity,"Temp": Temperature})
			open("/usr/lib/cgi-bin/temp","w").write(k)
			return 0
		return 1

	GPIO.cleanup()


lo=1
while lo==1:
	try:
		lo= run()
	except:
		pass
	#print "ERR_CRC"
	#print "Humidity:"+ Humidity +"%"
        #print "Temperature:"+ Temperature +"C"

