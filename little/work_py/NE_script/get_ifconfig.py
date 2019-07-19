
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.200.180.58", 22, "admin", "admin1")

stdin, stdout, stderr = ssh.exec_command("ifconfig")
#Time = str(ssh.exec_command("date"))
#print(Time)
records = stdout.readlines()
#print records
# the result:   ['/home/fs\n']

stdin, stdout, stderr = ssh.exec_command("ls")
#print records

f = open('config.txt', 'a')

for each in records:
   try:
      #f.write(str(each)+ '\n')
      f.write(str(each))
   except:
      pass
f.close()