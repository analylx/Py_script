import time
import os
path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,ip_head):
    with open(file_path, 'a') as fi:
        fi.write("""set interfaces ge-ts14/2 unit {0} family inet address 172.18.{1}.58/24
set interfaces ge-ts14/2 unit {0} vlan-id-list {0}
set protocols multihop-bfd source 108.{1}.0.58 destination 108.{1}.0.52
""".format(unit,ip_head))


for unit in range(1,101):

	ip_head = unit
	do_write(unit,ip_head)
#	print "%d" %unit
#	print "%d" %ip_head

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
"""