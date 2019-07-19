#coding:utf-8
import os
import time
import shutil
from winpexpect import winspawn
import winpexpect
def ssh_login(user,NE_IP):
	host_user='%s@%s' %(user,NE_IP)
	child=winpexpect.winspawn('ssh',['-t', '-t',  '-o StrictHostKeyChecking=no', '-o UserKnownHostsFile=d:/null', host_user])
	os.remove('D:\\null')
	index=child.expect(['(?i)~#','connect timed out',winpexpect.EOF,winpexpect.TIMEOUT])
	if (index!=0):
		print 'Connect to %s failed' %NE_IP
		child.terminate(force=True)
	child.sendline('lsh')	
	#"(?i)>" ÆÚÍû¾ßÓÐ>µÄ×Ö·û³öÏÖ,¾Í·µ»ØIndex=0
	child.expect(['(?i)>'])
	#child.expect('root@mcp1800>')
	child.sendline('configure')
	#child.expect('root@mcp1800#')
	child.sendline('q')
	print 'login %s NE succeeded' %NE_IP
	return child
	
def get_log(child,cipsip,mcpip,NE_IP):
	child.sendline('set system services ftp enable-network') 
	child.sendline('commit')
	child.sendline('quit')
	child.sendline('quit')
	#Log's file_name
	log_Direct=NE_IP
	child.sendline('rm -rf %s/' %log_Direct)
	child.sendline('mkdir -m 777 /sdlog/%s/' %log_Direct)
	#ip1='169.254.3.4'
	child.sendline('telnet %s' %cipsip)
	child.expect(['(?i)login'])
	child.sendline('root')
	child.expect(['(?i)#'])	

	for file_name in ['dpkg_dps.log','dataplane.log','dpsXmsg.log.org','pxc.log','messages']:
		child.sendline('ftpput %s -u root -p root /sdlog/%s/%s /var/log/%s' %(mcpip,log_Direct,file_name,file_name))
		time.sleep(5)
		child.expect(['(?i)#'])
	print 'finish get log, and log was saved in /sdlog/%s' %log_Direct
	
if __name__ == '__main__':	
	command_log = open('D:\\command_log.txt', 'w+')	
	NE_IP=raw_input('Input NPT1800 IP like a.b.c.d\n')
	child=ssh_login('root',NE_IP)
	#ÊäÈëºÍÊä³ö¶¼ÊäÈëµ½logÖÐ
	#child.logfile=command_log
	#Ö»ÓÐÊä³ö£¬ÊäÈëµ½logÖÐ
	child.logfile_read=command_log
	#¹ýÂË³öÖ÷µÄCIPSºÍÖ÷µÄMCP
	child.sendline('run show chassis status | grep act')
	#Æ¥ÅäÖ÷µÄcsaºÍmsbÊÇ·ñÍ¬Ê±Îªactive
	index1=child.expect(['csa(.*?)msa',winpexpect.TIMEOUT])
	while 1:
		if index1==0:
			cipsip='169.254.3.4'
			mcpip='169.254.3.2'
			print 'active cips is csa'
			print 'active mcp is msa'
			#get log 
			get_log(child,cipsip,mcpip,NE_IP)
			break
		
		index2=child.expect(['csa(.*?)msb',winpexpect.TIMEOUT])
		if index2==0:
			cipsip='169.254.13.4'
			mcpip='169.254.13.3'
			print 'active cips is csa'
			print 'active mcp is msb'
			#get log 
			get_log(child,cipsip,mcpip,NE_IP)
			break
		
		index3=child.expect(['csb(.*?)msa',winpexpect.TIMEOUT])
		if index3==0:
			cipsip='169.254.4.5'
			mcpip='169.254.4.2'
			print 'active cips is csb'
			print 'active mcp is msa'
			#get log 
			get_log(child,cipsip,mcpip,NE_IP)
			break
		
		index4=child.expect(['csb(.*?)msb',winpexpect.TIMEOUT])
		if index4==0:
			cipsip='169.254.14.5'
			mcpip='169.254.14.3'
			print 'active cips is csb'
			print 'active mcp is msb'
			#get log 
			get_log(child,cipsip,mcpip,NE_IP)
			break
		
		print 'cannot find the active cips or mcp'
		break
	#close file
	command_log.close()
	#close child
	child.terminate(force=True)	
	
	









'''
#get log from server
server_path='\\\\172.18.98.91\\ems-npt\\logs'
serpath_store='C:\\emslog\\serverlog' 
if not os.path.exists(serpath_store):
    os.makedirs(serpath_store)
os.chdir(serpath_store)
for s in ['server.log','sys.log','notify.log','nptiam.log']:
	source_file=server_path + '\\' + s
	dest_file=s
	shutil.copyfile(source_file,dest_file)


#get log from client
clipath_store='C:\\emslog\\clientlog' 
if not os.path.exists(clipath_store):
	os.makedirs(clipath_store)	
	
client_path='C:\\EMS-NPT\\logs'
os.chdir(clipath_store)
for s in ['client_zgl.log']:
	source_file=client_path + '\\' + s
	dest_file=s
	shutil.copyfile(source_file,dest_file)
'''
