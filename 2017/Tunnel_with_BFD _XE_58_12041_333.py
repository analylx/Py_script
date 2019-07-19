import time

file_path = 'D:\Py_script\script\\BFD_tunne58_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))

def do_write(tunnel_name,tunnel_label,remote,interface1,tunnel_label_in):
    with open(file_path, 'a') as fi:
        fi.write('''set protocols mpls static tunnel bidirectional {0} control-channel-cos 7
set protocols mpls static tunnel bidirectional {0} head-and-tail main bfd minimum-receive-interval 3.33 minimum-transmit-interval 3.33 multiplier 3
set protocols mpls static tunnel bidirectional {0} head-and-tail main in-segment interface {3} label {4}
set protocols mpls static tunnel bidirectional {0} head-and-tail main out-segment interface {3} label {1}
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 7 eir 0Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options pir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 7 eir 0Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza pir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail to {2}
set protocols mpls static tunnel bidirectional {0} tunnel-id {0}
set protocols mpls static tunnel bidirectional {0} tunnel-num {0}\n''' .format(tunnel_name,tunnel_label,remote,interface1,tunnel_label_in))

n = 301
while n <= 600:
    tunnel_name = n + 37000
    tunnel_label = tunnel_name
    tunnel_label_in = n + 370000
    remote = '16.156.0.6'
    interface1 = 'xe-ts7/3.0'
    do_write(tunnel_name,tunnel_label,remote,interface1,tunnel_label_in)
    print "Create tunnel %d th to txt successful!" %n
    n+=1


