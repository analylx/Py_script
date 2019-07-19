import numbers
import time
import os

path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)   
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + "["+str(numbers.max_nmu) +"]"+ time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,IP1,IP2,interface1):
    with open(file_path, 'a') as fi:
        fi.write('''set interfaces {3} unit {0} vlan-id-list {0} family inet address 48.{1}.0.58/28
set protocols isis protocol-instance 0 interface {3}.{0} passive
set interfaces {3} unit {0} vlan-id-list {0} family iso
set interfaces {3} unit {0} family inet6 address 2001:48:{1}::58
''' .format(unit,IP1,IP2,interface1,interface1.split('.')[0]))

start_nmu = 2000
max_nmu = 2201

IP2 = 0
for n in range(start_nmu,max_nmu):
	unit = n
	IP1 = n - start_nmu
	IP2 = IP1/255
	IP1 = IP1%255

	interface1 = 'ge-ts15/1'
	do_write(unit,IP1,IP2,interface1)
	print "Create vrrp %d th to txt successful!" %n
	#n+=1
