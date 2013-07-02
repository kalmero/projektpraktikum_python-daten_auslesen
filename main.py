from sys import argv
import time
import threading

def rem_wrap(file_name):
	# removes the last character
	jo=file_name.read()
	jo = int(jo[0:len(jo)-1])
	return jo

def military_timestamp():
	#creates a military timestamp a la 1400
	localtime = time.localtime(time.time())
	if localtime.tm_hour < 10:
		hour= '0%s'%localtime.tm_hour
	else:
		hour='%s'%localtime.tm_hour
        
	if localtime.tm_min < 10:
		min='0%s'%localtime.tm_min
	else:
		min='%s'%localtime.tm_min

	return '%s%s'%(hour,min)

def date_timestamp():
	localtime = time.localtime(time.time())
	month = localtime.tm_mon
	day = localtime.tm_mday
	return '%s %s'%(day, month)

def read_first_line():
	target = open("measurements.txt")
	lines=target.readlines()
	first_line=lines[0]
	target.close()
	return first_line[0:-1]

def write_out(content):
	target = open("measurements.txt")
	print '%r'%date_timestamp()
	print '%r'%read_first_line()

	if read_first_line()==date_timestamp():
		print "Today's File"
		#if we are dealing with today's file
		target = open("measurements.txt","a") #append mode
		target.write(content)
	else:
		print "Not Today's File"
		target = open("measurements.txt","w") #(over)write mode
		target.write(date_timestamp())
		target.write(content)
	target.close()	


def measurement():
	global tmp
	global hum
	global pres
	global lux
	global count		#todo: check whether there should be a 0 instead
	
	tmp_file = open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0040/temp1_input")
	hum_file = open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0040/humidity1_input")
	pres_file= open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0077/pressure0_input")
	lux_file = open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0039/lux1_input")


	tmp = tmp + rem_wrap(tmp_file)
	hum = hum + rem_wrap(hum_file)
	pres = pres + rem_wrap(pres_file)
	lux = lux + rem_wrap(lux_file)
	tmp_file.close()
	hum_file.close()
	pres_file.close()
	lux_file.close()

	if count == 60:
		tmp=tmp/60	#calculate average
		hum=hum/60
		pres=pres/60
		lux=lux/60
		new_meas = "\n%s %s %s %s %s" % (military_timestamp(), tmp, hum, pres, lux)
		print new_meas
		write_out(new_meas)
		del tmp,hum,pres,lux,count	#reset variables

	else:
		count = count + 1
	timer = threading.Timer(1.0,measurement)
	timer.start()
	
timer = threading.Timer(1.0,measurement)
timer.start()
