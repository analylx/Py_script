import time

file_path = 'D:\Py_script\script\\BFD_PW_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(vsi_name,tunnel_label,remote,interface1,tunnel_label_in):
    with open(file_path, 'a') as fi:
        fi.write('''set interfaces ge-ts2/8 unit {0} family vpls
set interfaces ge-ts2/8 unit {0} vlan-id-list {0}
set switching-instances vpls {0} interface {3}
set switching-instances vpls {0} remote-tpe {2} oam cos 7
set switching-instances vpls {0} remote-tpe {2} peer-address {2}
set switching-instances vpls {0} remote-tpe {2} pw-status-tlv-enable
set switching-instances vpls {0} remote-tpe {2} pw-type ethernet
set switching-instances vpls {0} remote-tpe {2} static in-pw-label {1}
set switching-instances vpls {0} remote-tpe {2} static out-pw-label {4}
set switching-instances vpls {0} remote-tpe {2} static tunnel 37000
set switching-instances vpls {0} inni-svlan {0}
set switching-instances vpls {0} l2vpn-id {0}\n''' .format(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in))

n = 400
while n <= 699:
    vsi_name = n
    tunnel_label_out = n + 14000
    tunnel_label_in = n + 14000
    remote = '16.156.0.6'
    interface1 = 'ge-ts2/8.' + str(n)
    do_write(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in)
    print "Create vpls %d th to txt successful!" %n
    n+=1
