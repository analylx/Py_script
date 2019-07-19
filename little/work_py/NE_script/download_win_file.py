# -*- coding: utf-8 -*-
import os
import shutil

def copyfile_download(remote_path, local_path,file_name):
	print "--------copyfile_download---------"
	print "remote_path in the function copyfile_download:" , remote_path
	full_name = os.path.join(remote_path, file_name)
	print "local_path in the function copyfile_download:" , local_path #这个local_path前面的逗号两边没空格会被判定缩进不对
	try:
		shutil.copy(full_name, local_path)
	except Exception, e:
		print "put error"
		print e

if __name__ == "__main__":
	remote_path = r"\\netstore-ch\R&D TN China\R&D_Server\Version Management\Dev_Version\Version to V&V\NPTI\V7.0\V7.0.019"
	file_name = "NPT1200i_Emb_sha256"
	local = os.path.abspath(os.path.dirname(__file__))
	copyfile_download(remote_path,local,file_name)