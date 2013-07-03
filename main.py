from sys import argv
import time
import threading

class Readout_Sensors:
	
	def __init__(self):
		print "Im Constructor"
		self.measurement()
	
	def rem_wrap(self, file_name):
		# removes the last character
		jo=file_name.read()
		jo = int(jo[0:len(jo)-1])
		return jo

	def military_timestamp(self):
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

	def date_timestamp(self):
		localtime = time.localtime(time.time())
		month = localtime.tm_mon
		day = localtime.tm_mday
		return '%s %s'%(day, month)

	def read_first_line(self):
		target = open("measurements.txt")
		lines=target.readlines()
		first_line=lines[0]
		target.close()
		return first_line[0:-1]

	def write_out(self,content):
		target = open("measurements.txt")
		print '%r'%self.date_timestamp()
		print '%r'%self.read_first_line()

		if self.read_first_line()==self.date_timestamp():
			print "Today's File"
			#if we are dealing with today's file
			target = open("measurements.txt","a") #append mode
			target.write(content)
		else:
			print "Not Today's File"
			target = open("measurements.txt","w") #(over)write mode
			target.write(self.date_timestamp())
			target.write(content)
		target.close()	

	def measurement(self):
		tmp = 0
		hum = 0
		pres = 0
		lux = 0
		for i in range(60):
			start_time=time.time()
			tmp_file = open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0040/temp1_input")
			hum_file = open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0040/humidity1_input")
			pres_file= open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0077/pressure0_input")
			lux_file = open("/sys/devices/ocp.2/4819c000.i2c/i2c-1/1-0039/lux1_input")

			tmp = tmp + self.rem_wrap(tmp_file)
			hum = hum + self.rem_wrap(hum_file)
			pres = pres + self.rem_wrap(pres_file)
			lux = lux + self.rem_wrap(lux_file)
			
			tmp_file.close()
			hum_file.close()
			pres_file.close()
			lux_file.close()

			end_time=time.time()
			diff_time = end_time-start_time
			if diff_time > 1:
				print "Timeout! CPU needed %ss" %diff_time
			else:
				time.sleep(1-diff_time)
				#one loop iteration takes approximatly 1s

		tmp = tmp/60
		hum= hum/60
		pres = pres/60
		lux = lux/60
		
		new_meas = "\n%s %s %s %s %s" % (self.military_timestamp(), tmp, hum, pres, lux)
		print new_meas
		self.write_out(new_meas)
		
		self.measurement()

r = Readout_Sensors()
