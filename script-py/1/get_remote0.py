# -*- coding:utf-8 -*-
import paramiko, time
import re


def get_remote0(Host, Port=22, User='admin', Password='admin1'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(Host, Port, User, Password)
    chan = ssh.invoke_shell()
    chan.send('config\n')
    file_tosave = str(
        time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())))
    command_name = 'show |display-set |save /sdboot/' + file_tosave + '\n'
    chan.send(command_name)
    time.sleep(15)  #must wait for a while to execute the command
    chan.send('run start shell\n')
    chan.send('ls -l /sdboot/\n')
    file_name_list = chan.recv(5000)
    time.sleep(2)
    ssh.close()
    print '{0} is saved.'.format(
        file_tosave)  #just output the saved name, need check done


def get_ipv4_ip_addr(Host, Port=22, User='admin', Password='admin1'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(Host, Port, User, Password)
    chan = ssh.invoke_shell()
    chan.send('config\n')
    #file_tosave = str(time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time())))
    #command_name = 'show |display-set |save /sdboot/'+file_tosave+'\n'
    #chan.send(command_name)
    chan.send('run show interfaces | no-more\n')
    time.sleep(3)  #must wait for a while to execute the command
    #chan.send('run start shell\n')
    #chan.send('ls -l /sdboot/\n')
    ip_list = chan.recv(9000)
    time.sleep(3)
    ssh.close()
    #print '{0} is saved.'.format(file_name_list) #just output the saved name, need check done
    with open("ifconfig.txt", 'w') as f:
        f.write(ip_list)


def ip_list(ip_file):
    #ip_file = input("filename")
    file = open(ip_file, 'r')  #打开文件
    ip = re.compile(
        r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')  #筛选IP正则表达式
    context = file.readlines()  #读取文本内容（.readlines()自动将文件内容分析成一个行的列表）
    file.close()
    ip_list = []
    for iplist in context:
        for iprow in ip.findall(iplist):
            if iprow.find("255"):
                #if not iprow.startswith("255"):
                #去掉225.开头的ip地址.如果这里换成find那么找到返回开始的索引值，如果是在开头找到那索引就是0，后面的索引是其他值正值，否则返回-1。
                #但是-1是True！所以也是可以的。也就是说只有是0才会是False，才会跳过
                ip_list.append(iprow)
    ip_list.sort()  #原列表排序会改变源列表
    with open("ip_list.txt", 'a') as f:
        f.write("+++++++++++++++++++++++++++++++++++++++++" + "\n")
        for ipaddr in ip_list:
            f.write(str(ipaddr) + "\n")


if __name__ == '__main__':
    Host = "200.200.180.58"
    Port = 22
    User = "admin"
    Password = "admin1"
    get_remote0(Host, Port, User, Password)
