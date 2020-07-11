#! /usr/bin/env python
#coding=GB18030
import getpass
import os
import shutil
import sys
import time

import case_wrapper
from casebase import getReg
from checkName import check
import dirLocation

def _init_rmReport():
#检查日志文件是否存在
    path = dirLocation.searchDir('report')    #获取report路径
    print path
    files=os.listdir(path)
    for i in files:                     #删除report下所有文件
        d_path=os.path.join(path,i)
        if os.path.isfile(d_path):
            os.remove(d_path)
def _init_rmLog():
    filePath = getReg.getRegVal("workSpace")    #获取workspace
    filePath = filePath+'\\runtime\\'

    despath = getReg.getRegVal("workSpace")
    despath = despath+"\\temp\\"
    
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'   
    fileRes=filePath+fileName
    if os.path.exists(fileRes):             #删除执行QuikLab时产生的日志
        os.remove(fileRes)
    if os.path.exists(despath):             #删除临时安装文件下载文件夹
        shutil.rmtree(despath)

#检查用户名和工程名是否存在
    tpList=case_wrapper.readIniConfig('QuikLab3.0')
    ck=check()
    if ck.ckUname(tpList[1]) == 1 and ck.ckProName(ck.getProName(tpList[3])) == 0:  #检查用户名和工程名返回值
        pass
    else:
        exit()
    print "Init finish!"
if __name__=='__main__':
    _init_rmReport()


