#! /usr/bin/env python  
# -*- coding: UTF-8 -*- 

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
#RCPD异常类
paramiko.__version__
appdirs.__version__
packaging.__version__
packaging.version.__doc__
packaging.specifiers.__doc__
packaging.requirements.__doc__
pyasn1.type.__doc__
pyasn1.type.univ.__doc__
class RCPD_Exception(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value
 
#CFGD异常类
class CFGD_Exception(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value 
        
#check进程的函数，进程stuck会报异常，每ss(s>2)秒check一次
def check(hostname,ss):
    hostname=hostname
    port = 22
    username = 'admin'
    password = 'admin1'
    #os.chdir(r'C:\Users\cchen\Desktop')
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname,port,username,password)
    ssh=s.invoke_shell()
    ss-=2
    while(1):
        time.sleep(ss)
        ssh=s.invoke_shell()
        ssh.send('ps -ef\n')
        time.sleep(2)
        x = ssh.recv(10000)
        #print x
        pattern1=re.compile(r'(./rcpd|\[rcpd\])')
        rcpd=re.findall(pattern1,x)
        print 'rcpd state: ',rcpd,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        pattern2=re.compile(r'(./cfgd|\[cfgd\])')
        cfgd=re.findall(pattern2,x)
        print 'cfgd state: ',cfgd,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if not rcpd[0]=='./rcpd':
            try:
                raise RCPD_Exception('RCPD stuck')
            except RCPD_Exception,e:
                print e
                

        if not cfgd[0]=='./cfgd':
            try:
                raise CFGD_Exception('CFGD stuck')
            except CFGD_Exception,e:
                print e
          

if __name__=='__main__': 
    ss=int(raw_input('Please put into the interval checktime(larger than 2s)/s:'))
    ne=raw_input('Please put into the NE IP:(such as 200.200.180.18):')
    check(ne,ss)


