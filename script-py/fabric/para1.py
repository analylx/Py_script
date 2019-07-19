#!/usr/bin/env python
# -- coding = 'utf-8' --
# Author Allen Lee
# Python Version 3.5.1
# OS Windows 7
import paramiko,sys
#创建ssh对象
ssh = paramiko.SSHClient()
#自动添加不在know_hosts中的机器
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='200.200.151.56',port=22,username='admin',password='admin1')
#执行命令
stdin,stdout,stderr = ssh.exec_command('pwd')
#获取命令结果
result = stdout.readline()
sys.stdout.write(result)
#关闭连接
ssh.close()


#封装连接
transport = paramiko.Transport(('200.200.151.56',22))
transport.connect(username='admin',password='admin1')
#创建ssh客户端对象
ssh = paramiko.SSHClient()
ssh._transport = transport
#给标准输入输出错误输出赋值
stdin,stdout,stderr = ssh.exec_command('pwd')
#打印获取的结果
print(stdout.readline())

sftp = paramiko.SFTPClient.from_transport(transport)
#将resutl.txt 上传至服务器 /tmp/result.txt
sftp.put('~/resutl.txt','/tmp/result.txt')
#将result.txt 下载到本地
sftp.get('/tmp/result.txt','~/yours.txt')
transport.close()

#使用密钥的SFTP
my_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
transport = paramiko.Transport(('hostname',22))
transport.connect(username='Meta',pkey=my_key)
sftp = paramiko.SFTPClient.from_transport(transport)
#将resutl.txt 上传至服务器 /tmp/result.txt
sftp.put('~/resutl.txt','/tmp/result.txt')
#将result.txt 下载到本地
sftp.get('/tmp/result.txt','~/yours.txt')
transport.close()
