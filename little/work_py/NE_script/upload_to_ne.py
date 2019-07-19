# -*- coding: utf-8 -*-
#import sftp_ne
import paramiko
import os,time
'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("200.200.180.58", 22, "admin", "admin1")

stdin, stdout, stderr = ssh.exec_command("cd /sdboot/up/")
stdin, stdout, stderr = ssh.exec_command("lcd D:\1800version\v7\19")
stdin, stdout, stderr = ssh.exec_command("put logfilescript")
records = stdout.readlines()
print records
# the result:   ['/home/fs\n']
time.sleep(3)
stdin, stdout, stderr = ssh.exec_command("ls")
records = stdout.readlines()
print records
ssh.close()
'''
host = "200.200.151.56"
port = 22

sf = paramiko.Transport((host,port))
sf.connect(username = "admin",password = "admin1")
sftp = paramiko.SFTPClient.from_transport(sf)
sftp.put(r"D:\1800version\v7\19\logfilescript","/sdboot/up/logfilescript")

#sftp.sftp_upload()