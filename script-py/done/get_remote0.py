import paramiko,time

def get_remote0(Host,Port=22,User='admin',Password='admin1'):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(Host, Port, User, Password)

	chan = ssh.invoke_shell()
	chan.send('config\n')
	file_tosave = str(time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time())))
	command_name = 'show |display-set |save /sdboot/'+file_tosave+'\n'
	chan.send(command_name)
	time.sleep(15)#must wait for a while to execute the command
	chan.send('run start shell\n')
	chan.send('ls -l /sdboot/\n')
	file_name_list=chan.recv(5000)
	time.sleep(2)
	ssh.close()
	print '{0} is saved.'.format(file_tosave) #just output the saved name, need check done


if __name__ == '__main__':
	Host = "200.200.180.58"
	Port = 22
	User = "admin"
	Password = "admin1"
	get_remote0(Host,Port,User,Password)
