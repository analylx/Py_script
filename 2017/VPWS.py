file_path = 'E:\\Version\\vpws'
with open(file_path, 'a') as fi:
    fi.write('''interfaces {
    xe-ts4/2 {
        bpdu-destination-mac 802.1ad;
        mac-filtering-mode Disabled;
        mpls-tp-frr-options {
            hold-off-timer 0;
            wtr-timer 7;
        }
        max-frame-size 9122;
        vlan-tpid Tag-default;
        type {
            vlan-tagged {
                priority-tagged-frame-handling forward;
                pvid 1;
                untagged-frame-handling forward;
                untagged-frame-default-cos 0;
            }
        }\n''')



def do_write(Outlabel,Inlabel,n):
    with open(file_path, 'a') as fi:
        fi.write('''        unit %d {
            layer2-transport %d {
                customer Customer;
                description ;
                nms-service-id %d;
                nms-user-label UserLabel;
                l2-service-mtu 1500;
                pw-type ethernet;
                remote-tpe 0.0.0.1 {
                    hold-off-timer 0;
                    oam {
                        cos 7;
                        oam-refresh-timer 30;
                    }
                    peer-address 0.0.0.1;
                    pw-type ethernet;
                    static {
                        in-pw-label %d;
                        out-pw-label %d;
                        tunnel 1;
                    }
                }
                l2vpn-id %d;
            }
            qos-profile default;
            vlan-id-list %d;
            policer-options {
                no-rate-limit;
            }
        }\n''' %(n,p,p,Inlabel,Outlabel,p,n))

n = 2001
while n <= 4000:
    Outlabel = n + 11000
    Inlabel = n + 11000
    p =n
    do_write(Outlabel,Inlabel,n)
    print "Create VPWS %d th to txt successful!" %n
    n+=1

with open(file_path, 'a') as fi:
    fi.write('''    }
}''')































'''
def do_write(y,z):
    z = y+360472
    file_path = 'E:\\workspace\\txt\\Create many BD LSP head tail.txt'
    with open(file_path, 'a') as fi:
        fi.write("set protocols mpls static tunnel bidirectional L%d nms-tunnel-name L%dN tunnel-id %d head-and-tail main in-segment interface xe-ts10/1.1 label %d\n" %(y,y,y,z))
    with open(file_path, 'a') as fi:
        fi.write("set protocols mpls static tunnel bidirectional L%d nms-tunnel-name L%dN tunnel-id %d head-and-tail main out-segment interface xe-ts10/1.1 label %d\n" %(y,y,y,y))
    with open(file_path, 'a') as fi:
        fi.write("set protocols mpls static tunnel bidirectional L%d nms-tunnel-name L%dN tunnel-id %d head-and-tail to 2.2.2.2\n" %(y,y,y))
    with open(file_path, 'a') as fi:
        fi.write("commit\n")

    with open(file_path, 'a') as fi:
        fi.write("\n\n")


x = 16
while x <= 8015:
    y = x
    z = y +360472
    do_write(y,z)
    print "Create BD-LSP head tail %d  to txt successful!" %x
    x+=1
'''



