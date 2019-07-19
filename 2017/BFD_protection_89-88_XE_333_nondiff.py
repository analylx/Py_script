import time

file_path = 'D:\Py_script\script\\BFD_tunne58_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))

def do_write(tunnel_name,tunnel_label,remote,interface1,tunnel_label_p):
    with open(file_path, 'a') as fi:
        fi.write('''set protocols mpls static tunnel bidirectional {0} control-channel-cos 7
set protocols mpls static tunnel bidirectional {0} head-and-tail main bfd minimum-receive-interval 3.33 minimum-transmit-interval 3.33 multiplier 3
set protocols mpls static tunnel bidirectional {0} head-and-tail main in-segment interface {3} label {1}
set protocols mpls static tunnel bidirectional {0} head-and-tail main out-segment interface {3} label {1}
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 4 cir 50Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 4 eir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 7 eir 0Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options pir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 4 cir 50Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 4 eir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 7 eir 0Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza pir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail to {2}
set protocols mpls static tunnel bidirectional {0} tunnel-id {0}
set protocols mpls static tunnel bidirectional {0} tunnel-num {0}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection bfd minimum-receive-interval 3.33 minimum-transmit-interval 3.33 multiplier 3
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options cos 4 cir 50Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options cos 4 eir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options cos 7 eir 0Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options pir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza cos 4 cir 50Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza cos 4 eir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza cos 7 cir 2Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza cos 7 eir 0Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza pir NRL
set protocols mpls static tunnel bidirectional {0} head-and-tail protection in-segment interface {3} label {4}
set protocols mpls static tunnel bidirectional {0} head-and-tail protection out-segment interface {3} label {4}\n''' .format(tunnel_name,tunnel_label,remote,interface1,tunnel_label_p))

n = 40000
while n <= 40200:
    tunnel_name = n
    tunnel_label = tunnel_name*10
    tunnel_label_p = tunnel_label + 1
    remote = '58.58.58.58'
    interface1 = 'xe-ts11/2.0'
    do_write(tunnel_name,tunnel_label,remote,interface1,tunnel_label_p)
    print "Create tunnel %d th to txt successful!" %n
    n+=1
