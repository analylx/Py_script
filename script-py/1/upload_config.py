# -*- coding:utf-8 -*-
import paramiko
import time
import os
import glob


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
            print(data.strip())  #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err.strip())  #输出错误结果
            return err

    def exec_operational(self):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()


def upload(ne_ip='200.200.151.56'):
    ssh = paramiko.SSHClient()  #创建sshclient
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  #目的是接受不在本地Known_host文件下的主机。
    ssh.connect(ne_ip, 22, 'admin', 'admin1')
    chan = ssh.invoke_shell()
    chan.send('configure' + '\n')
    chan.send('show | display-set | save /sdboot/lastone' + '\n')
    time.sleep(15)
    ssh.put('./lastone', '/sdboot/lastone')
    return "configuration has saved to computer."
    time.sleep(3)
    res = chan.recv(4096)
    print(res)
    chan.close()


if __name__ == "__main__":
    ne_ip = '200.200.121.52'
    ne_type = '1200i'
    conn = SSHConnection(ne_ip, 22, 'admin', 'admin1')
    upload(ne_ip)
    conn.exec_command('ls -l')
    conn.download('/sdboot/lastone', './lastone_' + ne_type)

