import numbers
import time
import os

path1 = os.path.dirname(__file__)  
path2 = os.path.abspath(path1)    
file_path = path2 + "\\script\\"+ os.path.basename(__file__) + "["+str(numbers.max_nmu) +"]"+ time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(vsi_name,tunnel_label,remote,interface1,tunnel_label_in,interface0):
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
set switching-instances vpls {0} l2vpn-id {0}\n''' .format(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in,tunnel_used,interface0))

#n = numbers.start_nmu
#while n <= numbers.max_nmu:
for n in range(numbers.start_nmu,numbers.max_nmu):
    vsi_name = n + 2000
    tunnel_label_out = n + 20000
    tunnel_label_in = n + 20000
    remote = '0.58.0.58'
    interface0 = 'ge-ts2/5'
    interface1 = interface0+'.'+ str(n+2000)
    tunnel_used = 524
#    tunnel_used = n%100 + 40000
    do_write(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in,interface0)
    print "Create vpls %d th to txt successful!" %n
    n+=1
