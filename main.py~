from sys import argv
import time
import threading

def rem_wrap(file_name):
	# removes the last character
	jo=file_name.read()
	jo = jo[0:len(jo)-1]
	return jo

def measurement():
	localtime = time.localtime(time.time())

	tmp_file = open("measurements/tmp")
	hum_file = open("measurements/hum")
	pres_file= open("measurements/pres")
	lux_file = open("measurements/lux")

#The following Block removes the \n characters at the end of each measurement file
	tmp = rem_wrap(tmp_file)
	hum = rem_wrap(hum_file)
	pres = rem_wrap(pres_file)
	lux = rem_wrap(lux_file)

#Setting up the New Line
	new_meas = "%s%s %s %s %s %s" % (localtime.tm_hour, localtime.tm_min, tmp, hum, pres, lux)
	print new_meas
	timer.start()

timer = threading.Timer(3.0,measurement)
timer.start()
