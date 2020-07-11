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
#�����־�ļ��Ƿ����
    path = dirLocation.searchDir('report')    #��ȡreport·��
    print path
    files=os.listdir(path)
    for i in files:                     #ɾ��report�������ļ�
        d_path=os.path.join(path,i)
        if os.path.isfile(d_path):
            os.remove(d_path)
def _init_rmLog():
    filePath = getReg.getRegVal("workSpace")    #��ȡworkspace
    filePath = filePath+'\\runtime\\'

    despath = getReg.getRegVal("workSpace")
    despath = despath+"\\temp\\"
    
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'   
    fileRes=filePath+fileName
    if os.path.exists(fileRes):             #ɾ��ִ��QuikLabʱ��������־
        os.remove(fileRes)
    if os.path.exists(despath):             #ɾ����ʱ��װ�ļ������ļ���
        shutil.rmtree(despath)

#����û����͹������Ƿ����
    tpList=case_wrapper.readIniConfig('QuikLab3.0')
    ck=check()
    if ck.ckUname(tpList[1]) == 1 and ck.ckProName(ck.getProName(tpList[3])) == 0:  #����û����͹���������ֵ
        pass
    else:
        exit()
    print "Init finish!"
if __name__=='__main__':
    _init_rmReport()


