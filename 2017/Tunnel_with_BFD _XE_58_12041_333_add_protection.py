import time

file_path = 'D:\Py_script\script\\BFD_tunne58_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(tunnel_name,tunnel_label,remote,interface1,tunnel_label_in):
    with open(file_path, 'a') as fi:
        fi.write('''set protocols mpls static tunnel bidirectional {0} head-and-tail protection bfd minimum-receive-interval 3.33
set protocols mpls static tunnel bidirectional {0} head-and-tail protection bfd minimum-transmit-interval 3.33
set protocols mpls static tunnel bidirectional {0} head-and-tail protection bfd multiplier 3
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection in-segment interface {3}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection in-segment label {4}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection out-segment interface {3}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection out-segment label {1}\n''' .format(tunnel_name,tunnel_label,remote,interface1,tunnel_label_in))

n = 1
while n <= 600:
    tunnel_name = n + 37000 - 1
    tunnel_label = tunnel_name + 1
    tunnel_label_in = n + 370000
    remote = '16.156.0.6'
    interface1 = 'xe-ts10/1.0'
    do_write(tunnel_name,tunnel_label,remote,interface1,tunnel_label_in)
    print "Create tunnel %d th to txt successful!" %n
    n+=2


