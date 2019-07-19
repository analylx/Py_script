# -*- coding:utf-8 -*-
import re
def regresion_cips_so_ip_bfd():
    r1= re.compile(r"<\d.*>")
    with open("cips_app_1800.log",'r') as f:
        source = f.read()
        up_times= re.findall(r1,source)
    result= []
    for uptime in up_times:
        a= uptime.strip('<')
        b= a.strip('>')
        #print(b)
        if float(b)>1:
            result.append(b)
    return result
if __name__ == '__main__':
    result = regresion_cips_so_ip_bfd()
    print("number is :",result)