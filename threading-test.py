import threading
#Prints "who are you" every 3 seconds

def test():
	print "who are you?!"
	timer = threading.Timer(3.0,test)
	timer.start()

timer = threading.Timer(3.0,test)
timer.start()
