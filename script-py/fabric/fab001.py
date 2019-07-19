#!/usr/bin/env python
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
env.user = 'root'
env.hosts = ['192.168.1.23','192.168.1.24']
env.password = '123456'
 
@runs_once
def tar_task(): #本地打包任务函数，只限执行一次
  with lcd('/'):
    local("tar zcvf auto.tar.gz auto")
 
def put_task():
  run('mkdir /data') #上传任务函数
  with cd("/data"):
    with settings(warn_only=True):
      result = put("/auto.tar.gz","/data") #put上传出现异常时继续执行，非中止
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
      abort('Aboring file put task!') #出现异常时，确认用户是否继续
 
def check_task():
  with settings(warn_only=True):
    lmd5 = local("md5sum /auto.tar.gz",capture=True).split(' ')[0]
    rmd5 = run("md5sum /data/auto.tar.gz").split(' ')[0]
    if lmd5 == rmd5: #对比本地及远程文件MD5信息
      print "ok"
    else:
      print ERROR
def go():
  tar_task()
  put_task()
  check_task()   