# -*- coding: utf-8 -*-
import paramiko
import os

def sftp_upload(host,port,username,password,local,remote):
    sf = paramiko.Transport((host,port))
    sf.connect(username = username,password = password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local):#判断本地参数是目录还是文件
            for f in os.listdir(local):#遍历本地目录
                sftp.put(os.path.join(local+f),os.path.join(remote+f))#上传目录中的文件
        else:
            sftp.put(local,remote)#上传文件
    except Exception,e:
        print('upload exception:',e)
    sf.close()

def sftp_download(host,port,username,password,local,remote):
    sf = paramiko.Transport((host,port))
    sf.connect(username = username,password = password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local):#判断本地参数是目录还是文件
            for f in sftp.listdir(remote):#遍历远程目录
                 sftp.get(os.path.join(remote+f),os.path.join(local+f))#下载目录中文件
        else:
            sftp.get(remote,local)#下载文件
    except Exception,e:
        print('download exception:',e)
    sf.close()

if __name__ == '__main__':
    host = '200.200.151.56'#主机
    port = 22 #端口
    username = 'admin' #用户名
    password = 'admin1' #密码
    local = 'D:\1800version\v7\19\\' #本地文件或目录，与远程一致，当前为windows目录格式，window目录中间需要使用双斜线
    remote = '/opt/tianpy5/python/test/'#远程文件或目录，与本地一致，当前为linux目录格式
    sftp_upload(host,port,username,password,local,remote)#上传
    #sftp_download(host,port,username,password,local,remote)#下载