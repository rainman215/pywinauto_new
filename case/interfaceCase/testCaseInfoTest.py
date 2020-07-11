#! /usr/bin/env python
#coding=GB18030
'''
Created on 2019年2月19日

@author: KLJS044
'''
import ctypes
import json
import os
import time
import unittest

import casebase.getReg as regInfo
import data
from case.interfaceCase import readConfig


a='\x00' #C语言中的空格
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")

class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        lib.initQuiKLabPlatform()                 
        lib.loadProject(configList[4]) 

    @classmethod
    def tearDown(self):
        lib.releaseQuiKLabPlatform()
    @classmethod
    def testName_testCaseInfo(self):
        testCaseClassName  = testCaseName = classN = "t"*1024
        sqlInfo = data.check()
        testCaseClassName=sqlInfo.getTestCaseClassName(configList[4])       #从数据库获取测试用例类名称
        classCount = lib.getTestCaseClassCount()                            #从接口获取测试用例类总数

        
        for i in range(classCount):
            flag = 1
            lib.getTestCaseClassName(i, classN, len(classN))                #"根据索引，获取分类下的测试用例类名称"
            for sqlCaseClassName in testCaseClassName:
                i = sqlCaseClassName
#                 print "class=",i                           
                if classN.strip(a) == i.decode('utf-8').encode('GB18030'):  #从数据库获得的类名进行编码从unicode转成str                       #从接口获取的用例分类名与数据库内获得的用例分类名进行查找
                    flag = 0
                    sqlCaseName = sqlInfo.getTestCaseName(configList[4],i)  #从数据库获取测试用例名称
#                     print sqlCaseName 
                    caseCount = lib.getTestCaseCount(i.decode('utf-8').encode('GB18030')) #获取测试用例分类下测试用例数量
                    for c in range(caseCount):                              #调用接口遍历测试用例名称
                        caseFlag = 1
                        lib.getTestCaseName(i.decode('utf-8').encode('GB18030'),c,testCaseName,1024)  #根据索引c获取测试用例名称
                        for n in sqlCaseName:
                            if testCaseName.strip(a)==n:                    #数据库获得的用例名称和函数内获得的用例名称进行比较，找到匹配则caseFlag=0
                                caseFlag=0
                        if caseFlag == 1:                                   #数据库和函数获得的数据不匹配直接退出遍历
                            break

            if flag == 1:
                break
        assert flag == 0,"获取测试用例分类失败！"
        print "获取测试用例分类成功！" 
        assert caseFlag == 0,"获取测试用例名称失败！"
        print "获取测试用例名称成功！"                                           #获取用例失败时进行断言                                              #获取用例名称时进行断言

if __name__ == "__main__":
    unittest.main()