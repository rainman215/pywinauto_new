#! /usr/bin/env python
#coding=GB18030

'''
Created on 2019��2��27��

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


a='\x00' #C�����еĿո�
configList = readConfig.readIniConfig('QuikLab3.0')
installSpace=regInfo.getRegVal("applicationPath")
workSpace=regInfo.getRegVal("workSpace")
# os.chdir(installSpace)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")
R=data.check()
sqlProName=R.getProName()    #���ݿ��ȡ��������
class Test(unittest.TestCase):


    def setUp(self):
        lib.initQuiKLabPlatform()


    def tearDown(self):
        lib.releaseQuiKLabPlatform()


    def testName1_proInfo(self):

         
        count=lib.getProjectCount()  #�ӿں�����ȡ��������
        print '���ݿ⹤����:'+str(count)
        proName = 't' * 1024
        for i in range(count):          #����������
            flag=0
            lib.getProjectName(i,proName,len(proName))  #�ӿں�����ȡ��������
#             print proName.strip(a)
 
            #�жϽӿں�����ȡ�Ĺ������������ݿ��¹��������Ƿ�ƥ��
            for tempName in sqlProName:   
                if proName.strip(a) == tempName.decode('utf-8').encode('GB18030'):
                    flag=1      #����ƥ��
            if flag == 0:   
                print proName.strip(a) 
                break 
        if flag==0:
            print "�ӿ������ݿ⹤����Ϣ��ƥ��"
            assert flag == 1
        else:
            print '�ӿ������ݿ⹤����Ϣƥ��ɹ�'       
        
    def testName2_exportTest(self):    
        #����������Ϣ         
        folder_name=r'TestcaseInfo'
#         print type(workSpace)
        path = workSpace.encode('GB18030')+'\\'+folder_name     #workSpace����Ϊunicode,��ת����str
        if not os.path.exists(path):
            os.mkdir(os.path.join(workSpace,folder_name))       #��workSpace·���´���TestCaseInfo�ļ���
#             os.mkdir(os.path.join(path))              

#         name=raw_input('�������赼��������Ϣ�Ĺ�������:')    #raw_input���������뿴���ַ�������
        name = 'ZF_1111'
        if name in sqlProName:
            TestCase=lib.exportTestCaseInfo(path,name)    #�ӿڵ���������Ϣ
        else:         
            print '����Ĺ������Ʋ����ڣ��޷�����������Ϣ��'

        file_testcase_name=r'testcaseset.xml'
        file_testtask_name=r'testtaskset.xml'
        path_tastcase=path+'\\'+file_testcase_name            #����������Ϣtestcaseset.xml·��
        path_tasttask=path+'\\'+file_testtask_name            #����������Ϣtesttaskset.xml·��
        path_list=[path_tastcase,path_tasttask]
        
        #�жϴ洢·�����Ƿ����testcaseset.xml/testtaskset.xml�ļ�
        for i in range(len(path_list)):            
            if os.path.exists(path_list[i]):
                print '�洢·����'+path_list[i]+'�´���xml�ļ�,����������Ϣ�ɹ���'
            else:
                print '�洢·������xml�ļ�,����������Ϣʧ�ܣ�'
                assert os.path.exists(path_tastcase)== True
                        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()