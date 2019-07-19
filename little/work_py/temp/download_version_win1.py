# -*- coding: utf-8 -*-
# pip install shutil 这个是标准库，根本不需要额外加载
import os
import sys
import shutil
from datetime import datetime

# 替换为空
replace_sharepath = r"\\netstore-ch\R&D TN China\R&D_Server\Version Management\Dev_Version\Version to V&V\NPTI\V7.0\V7.0.019"


# 打开共享文件夹,从服务器下载文件
def win_download():
    path = r"\\netstore-ch\R&D TN China\R&D_Server\Version Management\Dev_Version\Version to V&V\NPTI\V7.0\V7.0.019"
    print "%s :%s" % (datetime.now(), path)
    print "local script real pathis :",os.path.realpath(sys.argv[0])
    print "local dir",os.path.split(os.path.realpath(sys.argv[0]))[0]
    try:
        print u"read dir wait...."
        getfiledir_download(path, "")
    except Exception, e:
        print "error : %s" % e

# 下载
def getfiledir_download(sharpath, childpath):
    print "getfiledir_download sharepath:",sharpath
    print "getfiledir_download childpath:",childpath
    try:
        childspath = ""
        filelist = os.listdir(sharpath)
        for files in filelist:
            filespath = os.path.join(sharpath, files)
            if os.path.isfile(filespath):   # 为文件
                print "server path:",filespath
                childspath = childpath
                print "server child path",childspath
                # 如果是文件，则复制
                copyfile_download(filespath, childspath)
            elif os.path.isdir(filespath):  # 为文件夹
                # print filespath
                childspath = os.path.join(childpath, files)
                # 如果为文件夹，则继续循环
                getfiledir_download(filespath, childspath)

    except Exception, e:
        print "download error: %s" % e

# 复制文件 或 文件夹 至本地存放
def copyfile_download(paths, childpath):
    print "path in the function copyfile_download:",paths
    print "child path in the function copyfile_download:",childpath
    localpath = os.path.split(os.path.realpath(sys.argv[0]))[0]
    putpath = path(paths, localpath, replace_sharepath)
    try:
        shutil.copy(paths, putpath)
    except Exception, e:
        print "put error"
        print e

# 拼接绝对路径
def path(sharpath, localpat, replacepath):
    sharpath_split = str(sharpath).split('\\')
    for i in sharpath_split:
        if i == None or i == "":
            continue
        else:
            if i in localpat:
                realpath = localpat.split(i)[0]
                return realpath + sharpath.replace(replacepath, "")

if __name__ == "__main__":
    share = r"\\netstore-ch\R&D TN China\R&D_Server\Version Management\Dev_Version\Version to V&V\NPTI\V7.0\V7.0.019"
    print "share in main:",share
    local = os.path.dirname(__file__)
    print "local in main:",local
    path = path(share, local, replace_sharepath)
    print "path in main:",path
    win_download()