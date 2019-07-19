#!/usr/bin/python
# -*- coding: UTF-8 -*-   
#########start 获取文件路径、文件名、后缀名############
def get_filePath_fileName_fileExt(filename):  
    (filepath,tempfilename) = os.path.split(filename);  
    (shotname,extension) = os.path.splitext(tempfilename);  
    return filepath,shotname,extension 
#########end 获取文件路径、文件名、后缀名############  
import os


start_nmu = 2000
max_nmu = 2050




