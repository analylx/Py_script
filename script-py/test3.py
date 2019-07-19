import time,re

r1=re.compile(r"(([0-9a-fA-F]{1,4}):{1,2}){1,7}[0-9a-fA-F]{0,4}")
text= """
Routing-Instance:master
  Interface:xe-ts13/1.3900
    Prefix                                      Origin                                      Status
    3900::58/64                                 Configured                                  Unknown
    3902::58/64                                 Configured                                  Unknown
    3903::58/64                                 Configured                                  Unknown
    3904::58/64                                 Configured                                  Unknown
    fe80::220:8fff:fe00:586b/64                 Link-Local                                  Unknown
"""
for match in r1.findall(text):#这个和finditer返回不一样的原因应该是compile里面有group，findall会返回元组的列表，但这个不是期望值
    print('Found {!r}'.format(match))
"""for match in re.findall(r1,text):#和上句效果一模一样
    print('Found {!r}'.format(match))"""
print("*"*40)
for match in r1.finditer(text):#可以返回期望值，一个IPv6地址.要使用正确的函数方法
    s= match.start()
    e=match.end()
    print('Found {!r} at {} {}'.format(text[s:e],s,e))

r1=re.compile(r"abc")
text= "abd::abc::abcabcabc"
print (r1.findall(text))
for match in r1.finditer(text):
    s= match.start()
    e=match.end()
    print('Found {!r} at {} {}'.format(text[s:e],s,e))