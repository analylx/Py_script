import random
import socket
import struct


for num in range(10):
    #print (socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
    #print (':'.join('{:x}'.format(random.randint(0, 2**16 - 1)) for i in range(4)) + ':1')
    print (':'.join('{:x}'.format(random.randint(0, 2**16 - 1)) for i in range(4)) +':'+':'.join('{:x}'.format(random.randint(0, 2**16 - 1)) for i in range(4)))