import paramiko,glob

transport = paramiko.Transport(('200.200.121.52',22))
transport.connect(username='admin',password='admin1')
sftp = paramiko.SFTPClient.from_transport(transport)
file_to_put = glob.glob(r"e:/version/NPT1200*.bin")
sftp.put(file_to_put[0],'/sdboot/up/NPT1200i_Emb.bin')  #upload
transport.close()
