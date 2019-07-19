
import paramiko,time,re

def remove_control_chars(s):	
	control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
	control_char_re = re.compile('[%s]' % re.escape(control_chars))

	return control_char_re.sub('', s)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.200.180.58", 22, "root", "root")

#stdin, stdout, stderr = ssh.exec_command("lsh;configure;run show bfd session")
chan = ssh.invoke_shell()

chan.send('lsh\n')
chan.send('show bfd session \n')
time.sleep(3)
records = chan.recv(50000)
#print "records is " + str(records)
ssh.close()

f = open('18058.txt', 'a')

for each in records:
   try:
   	#f.write(str(each))
   	f.writelines(remove_control_chars(each))
   except:
      pass
f.close()