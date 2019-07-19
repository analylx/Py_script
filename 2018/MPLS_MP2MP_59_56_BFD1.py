import numbers
import time
import os

file_path = '\script' + os.path.basename(__file__) + "["+str(numbers.max_nmu) +"]"+ time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(vsi_name,tunnel_label,remote,interface1,tunnel_label_in):
    with open(file_path, 'a') as fi:
        fi.write('''set interfaces {6} unit {0} family vpls
set interfaces {6} unit {0} vlan-id-list {0}
set switching-instances vpls {0} nms-service-id {0}
set switching-instances vpls {0} interface {3}
set switching-instances vpls {0} remote-tpe {2} oam cos 7
set switching-instances vpls {0} remote-tpe {2} control-word
set switching-instances vpls {0} remote-tpe {2} oam bfd minimum-receive-interval 100 minimum-transmit-interval 100 multiplier 3 
set switching-instances vpls {0} remote-tpe {2} peer-address {2}
set switching-instances vpls {0} remote-tpe {2} pw-status-tlv-enable
set switching-instances vpls {0} remote-tpe {2} pw-type ethernet
set switching-instances vpls {0} remote-tpe {2} static in-pw-label {1}
set switching-instances vpls {0} remote-tpe {2} static out-pw-label {4}
set switching-instances vpls {0} remote-tpe {2} static tunnel {5}
set switching-instances vpls {0} inni-svlan {0}
set switching-instances vpls {0} l2vpn-id {0}\n''' .format(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in,tunnel_used,interface1.split('.')[0]))

#n = numbers.start_nmu
#while n <= numbers.max_nmu:
#start_nmu = 50800
#max_nmu = 51000
"""
if None != start_nmu:
	numbers.start_nmu = start_nmu
	numbers.max_nmu = max_nmu
"""
for n in range(numbers.start_nmu,numbers.max_nmu):
    vsi_name = n + 1000
    tunnel_label_out = n + 10000
    tunnel_label_in = n + 10000
    remote = '0.56.0.56'
    interface1 = 'ge-ts18/10.' + str(n+1000)
    tunnel_used = 46000
#    tunnel_used = n%100 + 40000
    do_write(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in)
    print "Create vpls %d th to txt successful!" %n
    n+=1
