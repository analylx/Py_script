import time
import os

file_path = 'D:\Py_script\little\\script_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,ip_head):
    with open(file_path, 'a') as fi:
        fi.write("""set protocols bfd ipv6 interface ge-ts23/1.{0} destination {1}::1/64
""".format(unit,ip_head))


for unit in range(10,210):

	ip_head = unit + 4000
	do_write(unit,ip_head)
#	print "%d" %unit
#	print "%d" %ip_head