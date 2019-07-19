# -*- coding:utf-8 -*-
import re


def regresion_cips_so_ip_bfd(sessions, interval=2):
    p_list = [0] * sessions
    d_list = []
    r1 = re.compile(r"Session up time.*")
    r2 = re.compile(r"Detect:.*,")
    with open("cips.txt", 'r') as f:
        source = f.read()
        up_times = re.findall(r1, source)
        detTimes = re.findall(r2, source)
    n = 0  #n还是需要从0开始的
    for uptime in up_times:
        #print(uptime.split(':')[:])=['Session up time', ' 1d 02', '58', '24'] ['Session up time', ' 00', '24', '06']
        #取出时间的分钟数，如果小于单次倒换的间隔，那么可以判断是发生震荡了.大于这个间隔就不是倒换造成的
        #并且高位的小时数不等于0
        if int(uptime.split(':')[2]) < interval and uptime.split(':')[1] == ' 00':
            p_list[n % sessions] += 1
        n += 1
    for detTime in detTimes[:sessions]:
        d_list.append(detTime.split(',')[0])
    return p_list, d_list


if __name__ == '__main__':
    p_list, d_list = regresion_cips_so_ip_bfd(10,3)
    #print(d_list)
    length = 1
    for p in p_list:
        print("session {0:>2}:{2}{1:^10} times flapping".format(
            length, p, d_list[length - 1]))
        length += 1