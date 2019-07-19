import numbers
import time
import os

path1 = os.path.dirname(__file__)  
#print 'The path1 is:', path1
path2 = os.path.abspath(path1)   
#print 'The path2 is:', path2   
#path3 = os.path.join(path2, 'hello.py')
#print 'The path3 is:', path3  
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + "["+str(numbers.max_nmu) +"]"+ time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,IP1,IP2,interface1):
    with open(file_path, 'a') as fi:
        fi.write('''set protocol bfd interface xe-ts13/1.{0} destination 2.{2}.{1}.81 minimum-receive-interval 3.33 minimum-transmit-interval 3.33 multiplier 3\n''' .format(unit,IP1,IP2,interface1,interface1.split('.')[0]))

#n = numbers.start_nmu
#while n <= numbers.max_nmu:
#start_nmu = 50800
#max_nmu = 51000
"""
if None != start_nmu:
	numbers.start_nmu = start_nmu
	numbers.max_nmu = max_nmu
"""
IP2 = 0
for n in range(numbers.start_nmu,numbers.max_nmu):
	unit = n
	IP1 = n
	IP2 = IP1/255
	IP1 = IP1%255

	interface1 = 'str'
	do_write(unit,IP1,IP2,interface1)
	print "Create vrrp %d th to txt successful!" %n
	#n+=1
