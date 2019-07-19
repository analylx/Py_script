#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import logging
# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
from getpass import getpass

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

net_connect = Netmiko(
    host="200.200.151.56",
    username="admin",
    password='admin1',
    device_type="cisco_ios",
)

print(net_connect.find_prompt())
net_connect.disconnect()