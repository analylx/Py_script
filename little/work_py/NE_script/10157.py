
import telnetlib,time

host = "200.200.101.57"
while True:
	tn = telnetlib.Telnet(host,"23")
	print tn
	#tn.read_until('login:')
	time.sleep(1)
	tn.write('root'+'\n')
	#tn.read_until('Password:')
	time.sleep(1)
	tn.write('root'+'\n')
	#tn.read_until("root>")
	time.sleep(1)
	tn.write('en\n')
	tn.write('switch shell\n')
	time.sleep(1)

	tn.write('memShow\n')
	time.sleep(3)
	records = tn.read_very_eager()
	time.sleep(5)
	tn.close()
	f = open('10157.txt', 'a')

	for each in records:
	   try:
	      f.write(str(each))
	   except:
	      pass
	f.close()
	time.sleep(1800)