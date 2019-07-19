# -*- coding:utf-8 -*-
import re
def regresion_cips_so_ip_bfd(sessions,interval=5):
    """
    sessions: int BFD进程数
    interval:int 倒换的间隔
    """
    p_list = [0]*sessions
    r1= re.compile(r"Session up time.*")
    r2= re.compile(r"Detect: \d*")
    with open("cips.txt",'r') as f:
        source = f.read()
        up_times= re.findall(r1,source)
        detect_list = re.findall(r2,source)
    n = 0#n还是需要从0开始的
    for uptime in up_times:
        #取出时间的分钟数，如果小于单次倒换的间隔，那么可以判断是发生震荡
        if int(uptime.split(':')[2])< (interval-1) and uptime.split(':')[1].find(" 00",0,3)== 0 :
            p_list[n%sessions]+=1
        n += 1
    return p_list,detect_list[:sessions]
    
def result_print(sessions):
    p_list,d = regresion_cips_so_ip_bfd(sessions)
    print(d)
    length = 1
    for p in p_list:
        print ("session {0:>3}: {2:^8} :{1:>3d} times flapping".format(length,p,d[length-1]))
        length += 1

if __name__ == '__main__':
    result_print(13)