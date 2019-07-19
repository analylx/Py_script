import time

file_path = 'D:\Py_script\script\\BFD_PW_' + time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))+".ps"

def do_write(vsi_name,tunnel_label,remote,interface1,tunnel_label_in):
    with open(file_path, 'a') as fi:
        fi.write('''delete protocols mpls static tunnel bidirectional {1} head-and-tail main bfd
delete protocols mpls static tunnel bidirectional {1} head-and-tail protection bfd\n''' .format(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in,tunnel_used))

n = 2
while n <= 600:
    vsi_name = n + 2000
    tunnel_label_out = n + 37000
    tunnel_label_in = n + 20000
    remote = '58.58.58.58'
    interface1 = 'ge-ts23/8.' + str(n+2000)
    tunnel_used = n%100 + 40000
    do_write(vsi_name,tunnel_label_out,remote,interface1,tunnel_label_in)
    print "Create vpls %d th to txt successful!" %n
    n+=2
