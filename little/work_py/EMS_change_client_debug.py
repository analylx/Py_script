import re
import os

def change_client_debug():
	f=open('C:\EMS-NPT\etc\\client.properties','r+')
	alllines=f.readlines()
	f.close()
	f=open('C:\EMS-NPT\etc\\client.properties','w+')

	for eachline in alllines:
	    a=re.sub('debug = false','debug = true',eachline)
	    f.writelines(a)
	f.close()
if __name__ == '__main__':
	change_client_debug()