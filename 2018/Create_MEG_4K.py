import time
import os
path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"


def do_write(unit):
    with open(file_path, 'a') as fi:
        fi.write("""set protocols oam mpls g8113p1 meg {0} meg-id-format-options icc-based icc {0}
set protocols oam mpls g8113p1 meg {0} meg-id-format-options icc-based umc {0}
""".format(unit))


for unit in range(1000,4999):
	do_write(unit)

"""
set protocols mpls static tunnel bidirectional 35659 head-and-tail main in-segment interface ge-ts15/3.1000
set protocols mpls static tunnel bidirectional 35659 head-and-tail main in-segment label 505659
set protocols mpls static tunnel bidirectional 35659 head-and-tail main out-segment interface ge-ts15/3.1000
set protocols mpls static tunnel bidirectional 35659 head-and-tail main out-segment label 505659
set protocols mpls static tunnel bidirectional 35659 head-and-tail to 0.56.0.56
set protocols mpls static tunnel bidirectional 35659 nms-tunnel-name 35659
set protocols mpls static tunnel bidirectional 35659 tunnel-id 35659
set protocols mpls static tunnel bidirectional 35659 tunnel-num 35659
set protocols mpls static tunnel bidirectional 35659 diffserv-enable

set protocols oam mpls g8113p1 meg 177 managed-object mpls-tp-bdlsp tunnel 4053 role main
"""
