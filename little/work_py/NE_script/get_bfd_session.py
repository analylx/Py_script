
import paramiko,time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.200.180.61", 22, "admin", "admin1")

#stdin, stdout, stderr = ssh.exec_command("cd /;pwd")
#records1 = stdout.readlines()
#print records1

#stdin, stdout, stderr = ssh.exec_command("lsh;configure;run show bfd session")
chan = ssh.invoke_shell()

chan.send('lsh\n')
chan.send('run request debug "oswp bfd dump" \n')
time.sleep(100)
records = chan.recv(50000)
#records = stdout.readlines()
print "records is " + str(records)

ssh.close()
#stdin, stdout, stderr = ssh.exec_command("ls")


f = open('infoTieba.txt', 'a')

for each in records:
   try:
      f.write(str(each))
   except:
      pass
f.close()