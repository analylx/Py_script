# -*- coding: utf-8 -*-
import numbers
import time
import os

path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + "["+str(numbers.max_nmu) +"]"+ time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,ip_head):
    with open(file_path, 'a') as fi:
        fi.write("""set interfaces xe-xsa/4 unit {0} family inet6 address {1}::1/64
set interfaces xe-xsa/4 unit {0} vlan-id-list {0}
""".format(unit,ip_head))


for unit in range(1000,1999):

	ip_head = unit + 2000
	do_write(unit,ip_head)
#	print "%d" %unit
#	print "%d" %ip_head
