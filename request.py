import requests

def get_servertime(ip):
	request_time = requests.get(url = ip + ':8080/servertime')	
	server_time = request_time.content
	return server_time

print get_servertime('191.168.0.15')
