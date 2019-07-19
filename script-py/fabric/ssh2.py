# -*- coding:utf-8 -*-
import paramiko,time,os

class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    #下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print (data.strip())   #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print (err.strip())    #输出错误结果
            return err

    def exec_operational():
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

def copy_to_back_cips():
    ssh = paramiko.SSHClient() #创建sshclient
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #目的是接受不在本地Known_host文件下的主机。
    ssh.connect('200.200.151.56', 22, 'admin', 'admin1')
    chan=ssh.invoke_shell()#新函数
    chan.send('start shell'+'\n')
    chan.send('su'+'\n')
    chan.send('ftp 169.254.1.3'+'\n')
    time.sleep(1)
    chan.send('root'+'\n')
    time.sleep(1)
    chan.send('root'+'\n')
    time.sleep(1)
    chan.send('put /sdboot/up/NPT1050i_Emb.bin /sdboot/up/NPT1050i_Emb.bin'+'\n')
    time.sleep(30)
    chan.send('bye'+'\n')
    chan.send('exit'+'\n')
    chan.send('exit'+'\n')
    chan.send('configure'+'\n')
    chan.send('show | display-set | save /sdboot/lastone'+'\n')
    chan.send('run request reset ne'+'\n')
    time.sleep(1)
    chan.send('yes'+'\n')
    time.sleep(15)
    res=chan.recv(4096)#非必须，接受返回消息
    print(res)
    chan.close()

if __name__ == "__main__":
    conn = SSHConnection('200.200.151.56', 22, 'admin', 'admin1')
    conn.exec_command('cd /sdboot/up;pwd')  #cd需要特别处理
    conn.put('e:/version/NPT1050i_Emb.bin','/sdboot/up/NPT1050i_Emb.bin')
    conn.exec_command('ls -l')
    #下面是把版本传到备卡的主目录
    copy_to_back_cips()

