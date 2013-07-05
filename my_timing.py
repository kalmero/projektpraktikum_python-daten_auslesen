import sched
import time
import thread

s = sched.scheduler(time.time,time.sleep)

def measurement():
	global count
	print "%s Measurement dummy data... %s" %(time.time(),count)
	if count == 10:
		pass
		count = 1
	else:
		count += 1
		s.enter(1,1,measurement, ())
		s.run()

def write_out():
	global count
	last_time = time.time()
	print "%s Calculating Average ... and writing out" %time.time()
	#s.enter(10,1,write_out,())
	#s.run()
	return

def start_everything():
	s.enter(0,1,measurement,())
	s.enter(10,1,write_out,())
	s.run()

def check_the_gap():
	print "What gap?!"
	#well ...

global count
count = 1
try:
	thread.start_new_thread(start_everything,())
	thread.start_new_thread(check_the_gap,())
except:
	print "Error: unable to start thread"

while 1:
	pass
