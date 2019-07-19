
import paramiko,time,re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.200.180.58", 22, "root", "root")

#stdin, stdout, stderr = ssh.exec_command("lsh;configure;run show bfd session")
chan = ssh.invoke_shell()

chan.send('lsh\n')
chan.send('show bfd session \n')
time.sleep(3)
records = chan.recv(50000)
records = records.replace("[K","")
#print type(records)
#print "records is " + str(records)
ssh.close()

f = open('18058.txt', 'a')

for each in records:
   try:
   	#f.write(str(each))
   	#print each
   	f.writelines(each)
   except:
      pass
f.close()