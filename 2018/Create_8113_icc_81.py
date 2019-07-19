import time
import os
path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"


def do_write(unit,umc,mep):
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
set protocols oam mpls g8113p1 meg {0} meg-id-format-options icc-based icc {0}
set protocols oam mpls g8113p1 meg {0} meg-id-format-options icc-based umc {1}
set protocols oam mpls g8113p1 meg {0} managed-object mpls-tp-bdlsp tunnel {0} role main
set protocols oam mpls g8113p1 meg {0} mep {0} enable
set protocols oam mpls g8113p1 meg {0} remote-mep {2}
""".format(unit,umc,mep))


for unit in range(3187,3200):
    icc = unit
    umc = unit + 1000
    mep = unit + 2000
    do_write(unit,umc,mep)
