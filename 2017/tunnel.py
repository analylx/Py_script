file_path = 'D:\script\\tunnel'
with open(file_path, 'a') as fi:
    fi.write('''protocols {
    mpls {
        static {
            tunnel {
                bidirectional {\n''')

def do_write(n,Inlabel,Outlabel):
    with open(file_path, 'a') as fi:
        fi.write('''                    %d {
                        control-channel-cos 0;
                        description ;
                        head-and-tail {
                            main {
                                in-segment {
                                    interface ge-ts24/11.0;
                                    label %d;
                                }
                                out-segment {
                                    interface ge-ts24/11.0;
                                    label %d;
                                }
                                tm-options {
                                    cos 0 {
                                        cir 12Mbps;
                                        eir NRL;
                                    }
                                    pir NRL;
                                }
                                tm-optionsza {
                                    cos 0 {
                                        cir 14Mbps;
                                        eir NRL;
                                    }
                                    pir NRL;
                                }
                            }
                            to 0.0.1.1;
                        }
                        nms-tunnel-name %d;
                        nms-buffer ;
                        nms-tunnel-id "{1;1}";
                        tunnel-id %d;
                        tunnel-num %d;
                        customer Customer;}\n''' %(n,Inlabel,Outlabel,n,n,n))
    #fi.write("commit\n")
    #with open(file_path, 'a') as fi:
    #fi.write("\n\n")


n = 1
while n <= 2350:
    Inlabel = n + 360492
    Outlabel = n + 15
    do_write(n,Inlabel,Outlabel)
    print "Create VPLS %d th to txt successful!" %n
    n+=1

with open(file_path, 'a') as fi:
    fi.write('''}
           }
        }
    }
}''')

