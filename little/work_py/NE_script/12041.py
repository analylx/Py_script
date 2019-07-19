
import telnetlib,time

Host = "200.200.120.41"
tn = telnetlib.Telnet(Host,"23")
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
tn.write('switch output\n')
time.sleep(1)
tn.write('telnet 169.254.0.2\n')
time.sleep(1)
tn.write('me\n')
time.sleep(1)
tn.write('me\n')
time.sleep(1)
tn.write('go123456\n')
time.sleep(1)
tn.write('memShow\n')
time.sleep(2)
tn.write('mod_api_mem_dump\n')
time.sleep(10)
records = tn.read_very_eager()
#records = tn.read_all()
tn.close()
f = open('12041.txt', 'a')

for each in records:
   try:
      f.write(str(each))
   except:
      pass
f.close()