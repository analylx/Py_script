import re
import os

f=open('C:\EMS-NPT\etc\\client.properties','r+')  
alllines=f.readlines()  
f.close()  
f=open('C:\EMS-NPT\etc\\client.properties','w+')  
for eachline in alllines:  
    a=re.sub('#HostIP=127.0.0.1','HostIP=200.200.1.84',eachline)  
    f.writelines(a)  
f.close()