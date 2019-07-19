import time
import os
path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"


def do_write(unit,ip_head):
    with open(file_path, 'a') as fi:
        fi.write("""set protocols multihop-bfd ipv6 source {1}::56 destination {1}::58 minimum-receive-interval 100 minimum-transmit-interval 100 multiplier 3
""".format(unit,ip_head))


for unit in range(100,151):

	ip_head = unit + 4400
	do_write(unit,ip_head)
#	print "%d" %unit
#	print "%d" %ip_head