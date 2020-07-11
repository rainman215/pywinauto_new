#! /usr/bin/env python
#coding=GB18030
'''
Created on 2019年1月28日

@author: KLJS044
'''
import ctypes
import os
import time
import unittest

import casebase.getReg as regInfo
import data
import readConfig

a='\x00' #C语言中的空格
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
        print "获取对应目录上的文件个数:\n",count
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
            assert lib.getFileName(dir,i,fileName,len(fileName)) == 0,'获得资源文件名称失败'
            print "根据目录与文件索引，返回文件名称:\n",fileName
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
        assert lib.getFileContent(fileName,fileContent,len(fileContent)) == 0,'获得文件内容失败'
        print "修改之前根据文件名，返回文件内容:\n",fileContent
        
        setFileContent = '''<?xml version="1.0"?>
    <Layout>
        <Config mdiarea="0"/>
    </Layout>'''
        print "根据文件名，设置文件内容"
        assert lib.setFileContent(fileName,setFileContent) == 0,'设置文件内容失败'
#         fileContent = "fileContent"*300
        lib.getFileContent(fileName,fileContent2,len(fileContent))
        print "修改之后根据文件名，返回文件内容:\n",fileContent2


if __name__ == "__main__":
    unittest.main()