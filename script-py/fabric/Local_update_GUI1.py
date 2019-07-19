# -*- coding:utf-8 -*-
import paramiko
import time
import glob
import logging
import PySimpleGUI as sg

logging.basicConfig(filename='debug_log1300.log', level=logging.DEBUG)


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


def copy_to_backup_cips(ne_ip='200.200.180.58', ne_type='1800'):
    ssh = paramiko.SSHClient()  #创建sshclient
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  #目的是接受不在本地Known_host文件下的主机。
    ssh.connect(ne_ip, 22, 'admin', 'admin1')
    chan = ssh.invoke_shell()  #新函数
    main_cs = "a"
    chan.send('start shell' + '\n')
    chan.send('su' + '\n')
    #这里直接做个判断要是主用在b的话就把ip地址设置成169.254.1.2
    #先在前面run show chassis status找出主用cps，再判断执行哪个
    if main_cs == "b":
        chan.send('ftp 169.254.1.2' + '\n')
    else:
        chan.send('ftp 169.254.1.3' + '\n')
    time.sleep(1)
    chan.send('root' + '\n')
    time.sleep(1)
    chan.send('root' + '\n')
    time.sleep(1)
    put_cmd = 'put /sdboot/up/NPT' + ne_type + '_Emb.bin /sdboot/up/NPT' + ne_type + '_Emb.bin'
    chan.send(put_cmd + '\n')
    time.sleep(45)
    chan.send('ls' + '\n')
    chan.send('bye' + '\n')
    time.sleep(3)
    chan.send('sync' + '\n')
    chan.send('ls' + '\n')
    #res = chan.recv(4096)
    #logging.debug(res)
    chan.close()


#把版本传到主卡的主目录
def reboot_with_save(ne_ip='200.200.180.58', clear_config='no'):
    ssh = paramiko.SSHClient()  #创建sshclient
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  #目的是接受不在本地Known_host文件下的主机。
    ssh.connect(ne_ip, 22, 'admin', 'admin1')
    chan = ssh.invoke_shell()
    chan.send('configure' + '\n')
    chan.send('show | display-set | save /sdboot/lastone' + '\n')
    chan.send('sync' + '\n')  # 不需要等待，sync完成之前下发不了其他命令的...
    #chan.send('run request debug "no-recovery-reset sdh keep_rid"'+'\n')  #现阶段不怎么好用还不如重启两次快
    if clear_config == 'no':
        chan.send(
            'run request reset ne' + '\n')  # request reset no-recovery-sdh
    else:
        chan.send('request reset no-recovery-sdh' + '\n')
    time.sleep(1)
    chan.send('yes' + '\n')
    time.sleep(3)
    res = chan.recv(4096)
    logging.info(res)
    chan.close()


if __name__ == "__main__":
    #ne_ip = '200.200.130.81'
    #ne_type = '1300'
    form = sg.FlexForm('Simple data entry form')  # begin with a blank form
    layout = [[
        sg.Text(
            'Please enter NE IP, NE type (1800/1200i/1300/1050i),clear(yes or no)'
        )
    ], [sg.Text('Ne IP', size=(15, 1)),
        sg.InputText('200.200.130.81')],
              [sg.Text('Ne Type', size=(15, 1)),
               sg.InputText('1300')],
              [sg.Text('clear_config', size=(15, 1)),
               sg.InputText('no')], [sg.Submit(), sg.Cancel()]]
    button, values = form.LayoutAndRead(layout)
    ne_ip, ne_type, clear_config = values[0], values[1], values[2]
    conn = SSHConnection(ne_ip, 22, 'admin', 'admin1')
    #text = sg.PopupGetText('Title', 'Please input NE IP')
    #sg.Popup('The value returned from PopupGetText', ne_ip, ne_type)
    #加个临时变量filename把ne_type加到glob的参数里面去，后面加不加i都是可以的
    filename_pc = "e:/version/NPT" + ne_type + "*" + ".bin"
    file_to_put = glob.glob(filename_pc)
    #这个dest_file也是临时变量
    dest_file = '/sdboot/up/NPT' + ne_type + '_Emb.bin'
    conn.put(file_to_put[0], dest_file)
    conn.exec_command('pwd')

    copy_to_backup_cips(ne_ip, ne_type)
    conn.download('/sdboot/lastone',
                  './lastone_' + ne_type + time.asctime().replace(':', '-'))
    reboot_with_save(ne_ip, clear_config)
