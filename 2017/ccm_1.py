file_path = 'D:\Py_script\\ccm58'

def do_write(unit_change,MEP02,label_change):
    with open(file_path, 'a') as fi:
        fi.write('''set interfaces ge-ts2/6 unit {0} vlan-id-list {0}
set interfaces ge-ts2/6 unit {0} family vpls
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} ccm-options enable
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} ccm-options interval 100ms
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} cos 0
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} instance {0}
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} mep {1} enable
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} mep {1} direction up
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} mep {1} interface ge-ts2/6.{0}
set protocols oam ethernet cfm maintenance-domain 0 maintenance-association {0} remote-mep {0} destination-mac 00:00:00:00:00:00
set switching-instances vpls {0} interface ge-ts2/6.{0} role root
set switching-instances vpls {0} nms-service-id {0}
set switching-instances vpls {0} pw-type ethernet
set switching-instances vpls {0} remote-tpe 59.59.59.59 oam cos 7
set switching-instances vpls {0} remote-tpe 59.59.59.59 peer-address 59.59.59.59
set switching-instances vpls {0} remote-tpe 59.59.59.59 pw-type ethernet
set switching-instances vpls {0} remote-tpe 59.59.59.59 static in-pw-label {2}
set switching-instances vpls {0} remote-tpe 59.59.59.59 static out-pw-label {2}
set switching-instances vpls {0} remote-tpe 59.59.59.59 static tunnel {3}
set switching-instances vpls {0} l2vpn-id {0}\n''' .format(unit_change,MEP02,label_change,51000))

n = 1
while n <= 10:
    unit_change = n + 2000
    MEP02 = unit_change + 100
    label_change = n + 3100
    do_write(unit_change,MEP02,label_change)
    print "Create ccm %d th to txt successful!" %n
    n+=1

