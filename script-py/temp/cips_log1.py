# -*- coding:utf-8 -*-
#用re.search将符合条件的行打印出来，main中调用的时候输入参数为时间，单位是秒，可以输入1或者0.5等
import re

def regresion_cips_so_ip_bfd(time):
    result = []
    r1= re.compile(r"<\d.*>")
    with open("cips_app_1800.log",'r') as f:
        for line in f.readlines():
            sr = re.search(r1,line)
            if sr:
                a= sr.group().strip('<')
                b = a.strip('>')
                if float(b)>time:
                    result.append(line.strip())
    return result,time

if __name__ == '__main__':
    results,time = regresion_cips_so_ip_bfd(0.5)
    print("The time more than %d seconds,toatl %d:" %(time,len(results)))
    for result in results:
        print result