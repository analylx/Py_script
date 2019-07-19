import time

file_path = 'D:\Py_script\script\\BFD_tunne_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(tunnel_name,tunnel_label,remote,interface1,interface2,tunnel_label_p):
    with open(file_path, 'a') as fi:
        fi.write('''set protocols mpls static tunnel bidirectional {0} control-channel-cos 7
set protocols mpls static tunnel bidirectional {0} diffserv-enable
set protocols mpls static tunnel bidirectional {0} head-and-tail main bfd minimum-receive-interval 3.33 minimum-transmit-interval 3.33 multiplier 3
set protocols mpls static tunnel bidirectional {0} head-and-tail main in-segment interface {3} label {1}
set protocols mpls static tunnel bidirectional {0} head-and-tail main out-segment interface {3} label {1}
set protocols mpls static tunnel bidirectional {0} head-and-tail to {2}
set protocols mpls static tunnel bidirectional {0} tunnel-id {0}
set protocols mpls static tunnel bidirectional {0} tunnel-num {0}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection bfd minimum-receive-interval 3.33 minimum-transmit-interval 3.33 multiplier 3
set protocols mpls static tunnel bidirectional {0} head-and-tail protection in-segment interface {5} label {4}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection out-segment interface {5} label {4}\n''' .format(tunnel_name,tunnel_label,remote,interface1,tunnel_label_p,interface2))

n = 43000
while n <= 43999:
    tunnel_name = n
    tunnel_label = tunnel_name*10
    tunnel_label_p = tunnel_label + 1
    remote = '0.52.0.52'
    interface1 = 'xe-ts13/1.5'
    interface2 = 'ge-ts23/1.1'
    do_write(tunnel_name,tunnel_label,remote,interface1,interface2,tunnel_label_p)
    print "Create tunnel %d th to txt successful!" %n
    n+=1
