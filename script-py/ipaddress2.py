import ipaddress
def get_ip_network(ipaddr)
    my_ip = ipaddress.ip_interface(ipaddr.decode())
    my_ip_net = ipaddress.ip_network(my_ip,strict=False)
    return my_ip_net