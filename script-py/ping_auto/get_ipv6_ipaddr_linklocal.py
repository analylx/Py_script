# -*- coding:utf-8 -*-
import paramiko,time
import re
text = """admin@18058# run show ipv6 interfaces lifname xe-ts13/3.3500
Routing-Instance:master
  Interface:xe-ts13/3.3500
    Prefix                                      Origin                                      Status
    2001:1856:3500:1::58/64                     Configured                                  Assigned
    2001:1856:3500:2::58/64                     Configured                                  Assigned
    2001:1856:3500:3::58/64                     Configured                                  Assigned
    2001:1856:3500:4::58/64                     Configured                                  Assigned
    fe80::220:8fff:fe00:586d/64                 Link-Local                                  Assigned
"""
r1 = re.compile(r'fe80::220.{15}')
linklocal = re.findall(text)
print(linklocal[0])