import time
import os

file_path = 'D:\Py_script\little\\script_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,ip_head):
    with open(file_path, 'a') as fi:
        fi.write("""set interfaces ge-ts7/1 unit {0} family inet6 address {1}::52/64
set interfaces ge-ts7/1 unit {0} vlan-id-list {0}
""".format(unit,ip_head))


for unit in range(10,210):

	ip_head = unit + 4000
	do_write(unit,ip_head)
#	print "%d" %unit
#	print "%d" %ip_head