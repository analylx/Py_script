#main function
from get_remote0 import get_remote0

Host = "200.200.180.58"
Port = 22
User = "admin"
Password = "admin1"
hosts = ['200.200.180.58','200.200.151.56','200.200.130.81','202.202.120.52']

if __name__ == '__main__':

	for host in hosts:
		get_remote0(host,Port,User,Password)
	"""
	get_remote0('200.200.180.58',Port,User,Password)
	get_remote0('200.200.151.56',Port,User,Password)
	get_remote0('200.200.130.81',Port,User,Password)
	get_remote0('202.202.120.52',Port,User,Password)
	"""
	print "configuration is saved."
