import paramiko,glob

def put_file():
    transport = paramiko.Transport('200.200.121.52',22)
    transport.connect(username='admin',password='admin1')
    sftp = paramiko.SFTPClient.from_transport(transport)
    file_to_put = glob.glob(r"e:/version/NPT1200*.bin")
    sftp.put(file_to_put[0],'/sdlog/www/NPT1200i_Emb.bin')  #upload
    #将result.txt 下载到本地
    #sftp.get('/sdlog//lastone','./yours.txt')
    transport.close()

if __name__ == '__main__':
    put_file()