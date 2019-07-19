import time
import os
path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"


def do_write(unit,umc):
    with open(file_path, 'a') as fi:
        fi.write("""
set interfaces xe-ts2/3 unit {0} family mpls
set interfaces xe-ts2/3 unit {0} vlan-id-list {0}
set protocols mpls static tunnel bidirectional {0} head-and-tail main in-segment interface xe-ts2/3.{0}
set protocols mpls static tunnel bidirectional {0} head-and-tail main in-segment label 51{0}
set protocols mpls static tunnel bidirectional {0} head-and-tail main out-segment interface xe-ts2/3.{0}
set protocols mpls static tunnel bidirectional {0} head-and-tail main out-segment label 51{0}
set protocols mpls static tunnel bidirectional {0} head-and-tail to 0.58.0.58
set protocols mpls static tunnel bidirectional {0} nms-tunnel-name {0}
set protocols mpls static tunnel bidirectional {0} tunnel-id {0}
set protocols mpls static tunnel bidirectional {0} tunnel-num {0}
set protocols mpls static tunnel bidirectional {0} diffserv-enable
set protocols oam mpls g8113p1 meg {0} ccm-options enable
set protocols oam mpls g8113p1 meg {0} ccm-options interval 1s
set protocols oam mpls g8113p1 meg {0} cos 0
set protocols oam mpls g8113p1 meg {0} level 1
set protocols oam mpls g8113p1 meg {0} meg-id-format-options icc-based icc 3200
set protocols oam mpls g8113p1 meg {0} meg-id-format-options icc-based umc {1}
set protocols oam mpls g8113p1 meg {0} managed-object mpls-tp-bdlsp tunnel {0} role main
set protocols oam mpls g8113p1 meg {0} mep {0} enable
""".format(unit,umc))


for unit in range(3200,3265):
    umc = unit + 1000
    do_write(unit,umc)

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
