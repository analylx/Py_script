import paramiko,glob

transport = paramiko.Transport(('200.200.121.52',22))
transport.connect(username='admin',password='admin1')
sftp = paramiko.SFTPClient.from_transport(transport)
file_to_put = glob.glob(r"e:/version/NPT1050i*.bin")
#conn.put(file_to_put[0],'/sdboot/up/NPT1050i_Emb.bin')
#将resutl.txt 上传至服务器 /tmp/result.txt
sftp.put(file_to_put[0],'/sdboot/testesttest')
#将result.txt 下载到本地
#sftp.get('/tmp/result.txt','~/yours.txt')
transport.close()
