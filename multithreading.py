import time
import threading

class Upload_Data:

	def sowieso(self):
		print "sowieso"

	def zeit(self):
		time.sleep(2)
		print "nach 2 sec"

	run = threading.Thread(sowieso)
	run2 = threading.Thread(zeit)
	run.start()
	run2.start()
