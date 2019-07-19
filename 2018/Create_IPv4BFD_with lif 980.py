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
        fi.write('''set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0
set interfaces ge-ts2/1 unit {0} family mpls
set interfaces ge-ts2/1 unit {0} vlan-id-list {0}
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 advertise-interval 1
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 bfd
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 master
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 preemption-hold-time 0
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 priority 255
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 version V2
set interfaces ge-ts2/1 unit {0} family inet address 1.{2}.{1}.59/255.255.255.0 vrrp-group 1 virtual-address 1.{2}.{1}.59\n''' .format(unit,IP1,IP2,interface1,interface1.split('.')[0]))

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
