# -*- coding: utf-8 -*-
#from ftplib import FTP
import os
import telnetlib
import time
import shutil
import socket
#import pdb
import paramiko
from Tkinter import *
import glob


def get_version_path(n1, n2, n3):
    if (int(n2) == 0):
        n11 = n1
        print('Upgrade version is v5.0 version')
    if (int(n2) == 1):
        n11 = n1 + '.' + n2
        print('Upgrade version is v5.1 version')
    if (int(n2) == 5):
        n11 = n1 + '.' + n2
        print('Upgrade version is v5.5 version')

    #判断是Temp version or official version
    if int(n3) > 500:
        server_path_tp1 = '\\\\172.18.104.44\\R&D TN China\\R&D_Server\\Version Management\\Dev_Version\\TempVersion\\NPTI\\' + 'V' + n11 + '\\' + versionNUM
        print 'version is a temp version'
    else:
        server_path_tp1 = '\\\\172.18.104.44\\R&D TN China\\R&D_Server\\Version Management\\Dev_Version\\Version to V&V\\NPTI\\' + 'V' + n11 + '\\' + 'V' + versionNUM
        print 'version is official vesion'
        #print server_path_tp1
    server_path_tp2 = server_path_tp1 + '*'

    #通过通配符函数，通配名字"NPT/NPT-1800/V5.1/versionNUM*的路径。
    #print server_path_tp2
    server_path_tp3 = glob.glob(server_path_tp2)
    server_path_tp4 = server_path_tp3[0]
    server_path = str(server_path_tp4)

    #print server_path

    print('Version path in server:%s' % server_path)
    #print os.listdir(server_path)
    #print os.getcwd()
    #判断’D:\\version\\NPT\\1800‘是否存在
    path = 'D:\\version\\NPT\\1800'
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(r'D:\\version\\NPT\\1800')
    return server_path


def sftp_get_version(version_type, server_path, hostname):

    os.chdir('D:\\version\\NPT\\1800')
    s = n1 + n2 + n3
    #print ('version_type is %d' %version_type)
    if version_type == 1:
        source_file = server_path + '\\' + 'NPT1800_Emb_' + s + '.bin'
        print('source_file is %s' % source_file)
    if version_type == 2:
        source_file = server_path + '\\' + 'NPT1800_Emb_2p0_' + s + '.bin'
        print('source_file is %s' % source_file)
    dest_file = 'NPT1800_Emb.bin'
    print 'Start get version ...........\n'
    shutil.copyfile(source_file, dest_file)
    print 'Get version successfully\n'

    try:
        sftp_port = 22
        username = 'root'
        password = 'root'
        t = paramiko.Transport(hostname, sftp_port)
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        local_dir = 'D:\\version\\NPT\\1800\\'
        remote_dir = '/sdboot/up/'
        dest_file = 'NPT1800_Emb.bin'
        print 'Start upload new version ......'
        sftp.put(
            os.path.join(local_dir, dest_file),
            os.path.join(remote_dir, dest_file))
        t.close()
        print 'upload new version successful'
    except:
        print "upload new version fail"
        t.close()


if __name__ == '__main__':
    hostname = raw_input('Input NPT1800 IP like a.b.c.d\n')

    versionNUM = raw_input(
        'Input the full name of versionNUM like 5.0.018 please input 5.0.018 \n'
    )
    version_type = int(raw_input('1+1 mode input 1;2+0 mode input 2\n'))

    listNum = versionNUM.split('.', )
    n1 = listNum[0]
    n2 = listNum[1]
    n3 = listNum[2]
    server_path = get_version_path(n1, n2, n3)

    sftp_get_version(version_type, server_path, hostname)

    #记录ssh 登录日志
    paramiko.util.log_to_file("log.log")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.connect("某IP地址",22,"用户名", "口令")
    ssh.connect(hostname, 22, "root", "root")
    #sh 登录到NE，设置FTP连接权限：
    '''
	stdin, stdout, stderr = ssh.exec_command("/etc/init.d/xinetd stop")
	stdin, stdout, stderr = ssh.exec_command("tcpsvd 0 21 ftpd -w /ftppub &")
	stdin, stdout, stderr = ssh.exec_command("/etc/init.d/xinetd start") 
	'''
    #修改startup文件
    stdin, stdout, stderr = ssh.exec_command(
        "sed -i 's/down/up/g' /sdboot/startup")

    print "start sync version.........."
    stdin, stdout, stderr = ssh.exec_command("sync")
    print stdout.readline()
    print "finish sync version"

    ssh.close()
    raw_input('press any key to exit \n')
