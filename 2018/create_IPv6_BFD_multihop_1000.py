import time
import os

file_path = 'D:\Py_script\little\\script_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(unit,ip_head):
    with open(file_path, 'a') as fi:
        fi.write("""set protocols multihop-bfd ipv6 source {1}::1 destination {1}::2
""".format(unit,ip_head))


for unit in range(1,100):

	ip_head = unit + 3000
	do_write(unit,ip_head)
#	print "%d" %unit
#	print "%d" %ip_head