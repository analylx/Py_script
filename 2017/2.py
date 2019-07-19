import time

file_path = 'D:\Py_script\script\\BFD_tunne_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(tunnel_name,tunnel_label,remote,interface1,interface2,tunnel_label_p):
    with open(file_path, 'a') as fi:
        fi.write('''set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-options cos 7 cir 10Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail main tm-optionsza cos 7 cir 10Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-options cos 7 cir 10Mbps
set protocols mpls static tunnel bidirectional {0} head-and-tail protection tm-optionsza cos 7 cir 10Mbps\n''' .format(tunnel_name,tunnel_label,remote,interface1,tunnel_label_p,interface2))

n = 40000
while n <= 40100:
    tunnel_name = n
    tunnel_label = tunnel_name*10
    tunnel_label_p = tunnel_label + 1
    remote = '58.58.58.58'
    interface1 = 'xe-ts13/2.0'
    interface2 = 'xe-ts13/4.0'
    do_write(tunnel_name,tunnel_label,remote,interface1,interface2,tunnel_label_p)
    print "Create tunnel %d th to txt successful!" %n
    n+=1
