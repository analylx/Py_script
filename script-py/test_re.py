# -*- coding:utf-8 -*-
import re
import ipaddress

source="""
Port: ge-ts2/1, Admin: disable, Oper: AdminDown
  Link Status: Down, Master Slave Res: Master
  PHY Type: 10/100/1000Base-T, Media Type: Copper
  AutoNeg: enabled
  Link-Mode: FULL
  Speed: 10M
  Flow Control Resolution: PauseReceive
  MAC Address: 00:20:8f:00:58:5f
  MRU: 9216
  Core ID: 1
  Expected Peer MAC: 00:00:00:00:00:00
  Received Peer MAC: 00:00:00:00:00:00
Routing-Instance:master
  Interface:xe-ts13/1.1
    Prefix                                      Origin                                      Status
    2AAA::58/64                                 Configured                                  Assigned
    fe80::220:8fff:fe00:586b/64                 Link-Local                                  Assigned
Routing-Instance:master
  Interface:xe-ts13/1.3800
    Prefix                                      Origin                                      Status
    2001:3881::58/64                            Configured                                  Assigned
    fe80::220:8fff:fe00:586b/64                 Link-Local                                  Assigned
Routing-Instance:master
  Interface:xe-ts13/1.3900
    Prefix                                      Origin                                      Status
    3900::58/64                                 Configured                                  Assigned
    fe80::220:8fff:fe00:586b/64                 Link-Local                                  Assigned
Routing-Instance:master
  Interface:xe-ts13/2.500
    Prefix                                      Origin                                      Status
    2001:5258::58/64                            Configured                                  Unknown
    fe80::220:8fff:fe00:586c/64                 Link-Local                                  Unknown
Routing-Instance:master
  Interface:xe-ts13/3.1
    Prefix                                      Origin                                      Status
    2010::58/64                                 Configured                                  Assigned
    fe80::220:8fff:fe00:586d/64                 Link-Local                                  Assigned
Routing-Instance:master
  Interface:xe-ts7/4.1000
    Prefix                                      Origin                                      Status
    2A00::58/64                                 Configured                                  Assigned
    fe80::220:8fff:fe00:586a/64                 Link-Local                                  Assigned
"""

#re.I表示忽略大小写
#\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b
#r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"  \b=单词边界；最后的[0-9]{1,3}=1-3个数字，独立出来是因为前面的内容是要带.的；
#最前面的?:=圆括号里面的内容不作为分组以便于后接数量词,如果不加的话会返回分组的最后一个组
#IPv6=r"(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])"
result4 = re.findall(r"\b(?:[1-9]\d?\.|1\d{2}\.|2[0-4]\d\.|25[0-2]\.)(?:[0-9]{1,3}\.){2}[0-9]{1,3}\b", source, re.I)#可用，但是会包含255的子网掩码
print ("IPv4 address list:",result4)
result6 = re.findall(r"(\b(?:[A-Fa-f0-9]{1,4}:{1,2}){1,7}[A-Fa-f0-9]{1,4}\/64\b)", source, re.I)#对于show ipv6 interface \/64 这段过滤出
print ("IPv6 address list:",result6)

Port_pattern=re.compile(r'(?:Port: [gx]e-[tx]s(?:\w+)\/(?:\d+))|(?:Port: mngb)|(?:Port: mnga)|(?:Port: auxmng)')	
Port_list=Port_pattern.findall(source)
print ("port list",Port_list)
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern?'
print('Text: {!r}\n'.format(text))#r表示raw，！表示r的转义

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')