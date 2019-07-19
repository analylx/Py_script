# -*- coding:utf-8 -*-
import re
def regresion_cips_so_ip_bfd(sessions,interval=2):
    p_list = [0]*sessions
    r1= re.compile(r"Session up time.*")
    with open("cips.txt",'r') as f:
        source = f.read()
        up_times= re.findall(r1,source)
    n = 0#n还是需要从0开始的
    for uptime in up_times:
        #print("minutes is :",uptime)
        #if n%sessions == 0:
        #    print ('')
        #取出时间的分钟数，如果小于单次倒换的间隔，那么可以判断是发生震荡了
        if int(uptime.split(':')[2])< interval:
            p_list[n%sessions]+=1
        n += 1
    return p_list

if __name__ == '__main__':
    p_list = regresion_cips_so_ip_bfd(6)
    length = 1
    for p in p_list:
        print ("session {0:>2}:{1:^10} times flapping".format(length,p))
        length += 1