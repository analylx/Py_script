# -*- coding:utf-8 -*-
#main function
from get_ipv6_ipaddr import Get_ipv6_ip_addr

Host = "200.200.180.58"
Port = 22
User = "admin"
Password = "admin1"
hosts = ['200.200.180.58','200.200.151.56','200.200.130.81','202.202.120.52']

if __name__ == '__main__':
    with open("ifconfig.rec",'w') as f:
        f.truncate()
    for host in hosts:
        Get_ipv6_ip_addr(host,Port,User,Password)
        #get_ipv4_ip_addr(host,Port,User,Password)
        #$ip_list("ifconfig.txt")

    print ("IPv6 address is saved.")
