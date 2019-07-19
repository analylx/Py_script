# -*- coding: utf-8 -*-
import paramiko,time,re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
DIP = raw_input("Please input an IP:")
ssh.connect(str(DIP), 22, "admin", "admin1")

#stdin, stdout, stderr = ssh.exec_command("lsh;configure;run show bfd session")
chan = ssh.invoke_shell()

#chan.send('lsh \n')
chan.send('configure \n')
chan.send('show | display-set | save /sdboot/'+time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+' \n')
time.sleep(3)
#records = chan.recv(50000)
#print "records is " + str(records)
ssh.close()
