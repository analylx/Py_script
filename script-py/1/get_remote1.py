import paramiko,time

def get_remote1(Host,Port,User,Password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(Host, Port, User, Password)
	return ssh
