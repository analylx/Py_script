# -*- coding:utf-8 -*-
#main function
from get_remote0 import *

Host = "200.200.180.58"
Port = 22
User = "admin"
Password = "admin1"
hosts = [
    '200.200.180.58', '200.200.151.56', '200.200.130.81', '200.200.121.52'
]

if __name__ == '__main__':

    for host in hosts:
        get_remote0(host, Port, User, Password)
        get_ipv4_ip_addr(host, Port, User, Password)
        ip_list("ifconfig.txt")

    print("configuration is saved.")
