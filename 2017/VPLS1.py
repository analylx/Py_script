file_path = 'D:\\Version\\vpls1'

with open(file_path, 'a') as fi:
    fi.write('''interfaces {
    ge-ts19/2 {
        bpdu-destination-mac 802.1ad;
        mac-filtering-mode Disabled;
        mpls-tp-frr-options {
            hold-off-timer 0;
            wtr-timer 7;
        }
        max-frame-size 9216;
        vlan-tpid Tag-default;
        type {
            vlan-tagged {
                priority-tagged-frame-handling forward;
                pvid 1;
                untagged-frame-handling forward;
                untagged-frame-default-cos 0;
            }
        }\n''')

def do_write_unit(n):
    with open(file_path, 'a') as fi:
        fi.write('''        unit %d {
            family vpls;
            qos-profile default;
            vlan-id-list %d;
            policer-options {
                no-rate-limit;
            }        
        }\n'''%(n,n))
        
def do_write_vpls(Outlabel,Inlabel,n):
    with open(file_path, 'a') as fi:
        fi.write('''switching-instances {
    vpls {
        %d {
            customer Customer;
            dai-options;
            description ;
            interface ge-ts19/2.%d {
                role root;
            }
            nms-service-id %d;
            nms-user-label UserLabel;
            l2-service-mtu 1500;
            pw-type ethernet;
            remote-tpe 0.0.0.1 {
                hold-off-timer 0;
                oam {
                    cos 0;
                    oam-refresh-timer 30;
                }
                peer-address 0.0.0.1;
                pw-type ethernet;
                split-horizon-group 1;
                static {
                    in-pw-label %d;
                    out-pw-label %d;
                    tunnel 1;
                }
                load-balance-flow-label disable;
            }
            vfib-quota 1;
            l2vpn-id %d;
        }
}
}\n'''%(n,n,n,Inlabel,Outlabel,n))

n = 4001
while n <= 4010:
    do_write_unit(n)
    print "Create unit %d th to txt successful!" %n
    n+=1

with open(file_path, 'a') as fi:
    fi.write('''    }
}\n''')

n = 4001
while n <= 4010:
    Outlabel = n + 9000+4000
    Inlabel = n + 9000 +4000
    do_write_vpls(Outlabel,Inlabel,n)
    print "Create VPLS %d th to txt successful!" %n
    n+=1
