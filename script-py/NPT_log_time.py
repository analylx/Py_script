
import telnetlib,time

def NPT_log_time():
    tn = telnetlib.Telnet("200.200.120.51","23")
    print ("1")
    time.sleep(1)
    tn.write('root\n')
    time.sleep(1)
    tn.write('root\n')
    time.sleep(1)
    tn.write('en\n')
    tn.write('switch output\n')
    time.sleep(1)
    tn.write('\n')
    tn.write('me\n')
    tn.write('go123456\n')
    print ("2")
    t3= 1
    while True:
        tn.write('NPSL_TblDispEntry 9\n')
        time.sleep(60)
        print(t3)
        t3 +=1
    tn.close()
    time.sleep(600)

if __name__ == '__main__':
    NPT_log_time()
