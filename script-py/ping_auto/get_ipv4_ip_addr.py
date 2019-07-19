# -*- coding:utf-8 -*-
import paramiko,time
import re

def get_ipv4_ip_addr(Host,Port=22,User='admin',Password='admin1'):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(Host, Port, User, Password)
	chan = ssh.invoke_shell()
	chan.send('config\n')
	#file_tosave = str(time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time())))
	#command_name = 'show |display-set |save /sdboot/'+file_tosave+'\n'
	#chan.send(command_name)
	chan.send('run show interfaces | no-more\n')
	time.sleep(3)#must wait for a while to execute the command
	#chan.send('run start shell\n')
	#chan.send('ls -l /sdboot/\n')
	ip_list=chan.recv(9000)
	time.sleep(3)
	ssh.close()
	#print '{0} is saved.'.format(file_name_list) #just output the saved name, need check done
	with open("ifconfig.rec", 'w+') as f:
		f.write(ip_list)


if __name__ == '__main__':
	Host = "200.200.180.58"
	Port = 22
	User = "admin"
	Password = "admin1"
	get_ipv4_ip_addr(Host)