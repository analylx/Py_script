
import telnetlib,time

def watch_dog_stop():
    tn = telnetlib.Telnet("200.200.105.98","23")
    print tn
    time.sleep(1)
    tn.write('root'+'\n')
    time.sleep(1)
    tn.write('root'+'\n')
    time.sleep(1)
    tn.write('en\n')
    tn.write('switch shell\n')
    time.sleep(1)
    tn.write('b Hmcp_feedDog\n')
    print "watch dog feed stop"
    tn.close()
    time.sleep(600)

if __name__ == '__main__':
    while(True):
        watch_dog_stop()
