import time
import os
path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"


def do_write(unit):
    with open(file_path, 'a') as fi:
        fi.write("""delete protocols bfd interface ge-ts14/2.{0}
""".format(unit))


for unit in range(1,100):
	do_write(unit)