#! /usr/bin/env python  
# -*- coding: UTF-8 -*- 

"""
The script is to check whether NE is in syncfail, if it is syncfail, login into CIPS to get login.


"""
import paramiko
import ssh
import os
import re
import time
import appdirs
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
import pyasn1.type
import pyasn1.type.univ

paramiko.__version__
appdirs.__version__
packaging.__version__
packaging.version.__doc__
packaging.specifiers.__doc__
packaging.requirements.__doc__
pyasn1.type.__doc__
pyasn1.type.univ.__doc__


#定义syncfail异常类
class Syncfail_Exception(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value
        
#定义
class syncfail(object):
    def __init__(slef,neip,cipsip,ss=5):
        slef.neip = neip
        slef.cipsip = cipsip
        slef.ss=ss
    def __str__(slef):
        print "Syncfail or not, is a question!"
        
    def checksyncfail(self):
        port = 22
        username = 'root'
        password = 'root'
        #os.chdir(r'C:\Users\cchen\Desktop')
        paramiko.util.log_to_file('paramiko.log')
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(self.neip,port,username,password)
        ssh=s.invoke_shell()
        self.ss-=2
        while(1):
            time.sleep(self.ss)
            ssh=s.invoke_shell()
            ssh.send('cat /var/log/dpkg_cfpal.log|grep syncfail\n')
            time.sleep(2)
            x = ssh.recv(10000)
            #print x
            pattern1=re.compile(r'(into syncfail state)')
            y=re.findall(pattern1,x)
            #y=1 just for test
            if y:
                print 'Syncfail occurs:\n',x,'\n',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            else:
                print 'No syncfail here.',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            
            if y:
                try:
                    raise Syncfail_Exception('Syncfail occurs')
                except Syncfail_Exception,e:
                    print e
                    self.getlog(self.neip,self.cipsip)
                    break
    def getlog(self,neip,cipsip):
        port = 22
        username = 'root'
        password = 'root'
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(self.neip,port,username,password)
        ssh=s.invoke_shell()
        ssh.send('/etc/init.d/xinetd stop\n\
        tcpsvd 0 21 ftpd -w /ftppub &\n\
        /etc/init.d/xinetd start\n')
        time.sleep(2)
        ssh.send('scp -vr root@'+cipsip+': /var/volatile/log/ /sdlog/\n')
        time.sleep(1)
        x1=ssh.recv(10000)
        print x1+'\n'
        pattern2=re.compile(r'Are you sure you want to continue connecting')
        y1=re.findall(pattern2,x1)
        if y1:
            ssh.send('yes\n')
            time.sleep(1)
            x2=ssh.recv(10000)
            print x2+'\n'
        
        print 'The log is in sdlog/log/ now.\n'


        
        
if __name__=='__main__':
    neip=raw_input('Please put in your NE IP, such as 200.200.180.24:')
    cipsip=raw_input('Please put in your CIPS IP:')
    ss=int(raw_input('Please put in the check interval time(s>3)'))
    sync=syncfail(neip,cipsip,ss)
    sync.checksyncfail()
    raw_input('Print any to quit!')