# -*- coding:utf-8 -*-

import re

def ip_list(ip_file):
    #ip_file = input("filename")
    file = open(ip_file,'r')  #打开文件
    ip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')  #筛选IP正则表达式
    context = file.readlines() #读取文本内容（.readlines()自动将文件内容分析成一个行的列表）
    file.close()
    ip_list= []
    for iplist in context:
        for iprow in ip.findall(iplist):
            if iprow.find("255"):
            #if not iprow.startswith("255"):
            #去掉225.开头的ip地址.如果这里换成find那么找到返回开始的索引值，如果是在开头找到那索引就是0，后面的索引是其他值正值，否则返回-1。
            #但是-1是True！所以也是可以的。也就是说只有是0才会是False，才会跳过
                ip_list.append(iprow)
    ip_list.sort()#原列表排序会改变源列表
    with open("ip_list.txt", 'w') as f:
        f.write("+++++++++++++++++++++++++++++++++++++++++"+"\n")
        for ipaddr in ip_list:
            f.write(str(ipaddr)+"\n")
if __name__ == '__main__':
    ip_list("ifconfig.txt")
