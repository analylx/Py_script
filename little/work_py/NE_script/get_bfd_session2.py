
import paramiko,time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.200.180.58", 22, "root", "root")

stdin, stdout, stderr = ssh.exec_command("lsh;configure;run show bfd session")

time.sleep(3)
records = stdout.readlines()

print "records is " + str(records)

ssh.close()

f = open('infoTieba.txt', 'a')

for each in records:
   try:
      f.write(str(each)+ '\n')
   except:
      pass
f.close()