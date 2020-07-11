#! /usr/bin/env python
#coding=GB18030

'''
Created on 2019年2月27日

@author: KLJS266
'''
import unittest
import ctypes
import json
import os
import time
import sys


import casebase.getReg as regInfo
import data
import readConfig


a='\x00' #C语言中的空格
configList = readConfig.readIniConfig('QuikLab3.0')
installSpace=regInfo.getRegVal("applicationPath")
workSpace=regInfo.getRegVal("workSpace")
# os.chdir(installSpace)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")
R=data.check()
sqlProName=R.getProName()    #数据库获取工程名称
class Test(unittest.TestCase):


    def setUp(self):
        lib.initQuiKLabPlatform()


    def tearDown(self):
        lib.releaseQuiKLabPlatform()


    def testName1_proInfo(self):

         
        count=lib.getProjectCount()  #接口函数获取工程数量
        print '数据库工程数:'+str(count)
        proName = 't' * 1024
        for i in range(count):          #遍历工程数
            flag=0
            lib.getProjectName(i,proName,len(proName))  #接口函数获取工程名称
#             print proName.strip(a)
 
            #判断接口函数获取的工程名称与数据库下工程名称是否匹配
            for tempName in sqlProName:   
                if proName.strip(a) == tempName.decode('utf-8').encode('GB18030'):
                    flag=1      #遍历匹配
            if flag == 0:   
                print proName.strip(a) 
                break 
        if flag==0:
            print "接口与数据库工程信息不匹配"
            assert flag == 1
        else:
            print '接口与数据库工程信息匹配成功'       
        
    def testName2_exportTest(self):    
        #导出用例信息         
        folder_name=r'TestcaseInfo'
#         print type(workSpace)
        path = workSpace.encode('GB18030')+'\\'+folder_name     #workSpace类型为unicode,需转换成str
        if not os.path.exists(path):
            os.mkdir(os.path.join(workSpace,folder_name))       #在workSpace路径下创建TestCaseInfo文件夹
#             os.mkdir(os.path.join(path))              

#         name=raw_input('请输入需导出用例信息的工程名称:')    #raw_input将所有输入看作字符串处理
        name = 'ZF_1111'
        if name in sqlProName:
            TestCase=lib.exportTestCaseInfo(path,name)    #接口导出用例信息
        else:         
            print '输入的工程名称不存在，无法导出用例信息！'

        file_testcase_name=r'testcaseset.xml'
        file_testtask_name=r'testtaskset.xml'
        path_tastcase=path+'\\'+file_testcase_name            #导出用例信息testcaseset.xml路径
        path_tasttask=path+'\\'+file_testtask_name            #导出用例信息testtaskset.xml路径
        path_list=[path_tastcase,path_tasttask]
        
        #判断存储路径下是否存在testcaseset.xml/testtaskset.xml文件
        for i in range(len(path_list)):            
            if os.path.exists(path_list[i]):
                print '存储路径：'+path_list[i]+'下存在xml文件,导出用例信息成功！'
            else:
                print '存储路径下无xml文件,导出用例信息失败！'
                assert os.path.exists(path_tastcase)== True
                        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()