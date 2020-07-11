#! /usr/bin/env python
#coding=GB18030
'''
Created on 2019��1��28��

@author: KLJS044
'''
import ctypes
import os
import time
import unittest

import casebase.getReg as regInfo
import data
import readConfig

a='\x00' #C�����еĿո�
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")

class Test(unittest.TestCase):


    def setUp(self):
        lib.initQuiKLabPlatform()                 
        lib.loadProject(configList[4]) 


    def tearDown(self):
        lib.releaseQuiKLabPlatform()


    def testName_fileResource(self):
        dir = "/"
        count=lib.getFileCount(dir)
        print "��ȡ��ӦĿ¼�ϵ��ļ�����:\n",count
        get_data=data.check()
        SqlList=get_data.getFileResources(configList[4])
        if count == len(SqlList):
            pass
        else:
            print "get File Count Wrong"
            exit()
        fileName = "fileName"*12
        flag=1
        for i in range(count):
            assert lib.getFileName(dir,i,fileName,len(fileName)) == 0,'�����Դ�ļ�����ʧ��'
            print "����Ŀ¼���ļ������������ļ�����:\n",fileName
            for c in SqlList:
                if fileName.strip(a).strip('/') == c:
                    flag=0
                else:
                    pass
            if flag==1:
#                 print fileName+"**********"
                break
        time.sleep(5)
        fileContent = fileContent2 = "fileContent"*300
        assert lib.getFileContent(fileName,fileContent,len(fileContent)) == 0,'����ļ�����ʧ��'
        print "�޸�֮ǰ�����ļ����������ļ�����:\n",fileContent
        
        setFileContent = '''<?xml version="1.0"?>
    <Layout>
        <Config mdiarea="0"/>
    </Layout>'''
        print "�����ļ����������ļ�����"
        assert lib.setFileContent(fileName,setFileContent) == 0,'�����ļ�����ʧ��'
#         fileContent = "fileContent"*300
        lib.getFileContent(fileName,fileContent2,len(fileContent))
        print "�޸�֮������ļ����������ļ�����:\n",fileContent2


if __name__ == "__main__":
    unittest.main()