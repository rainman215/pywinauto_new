#! /usr/bin/env python
#coding=GB18030
import getpass
import logging
import os
import unittest

from casebase import getReg
import casebase.case_wrapper as case


configList = case.readIniConfig('QuikLab3.0')
pyfilename = os.path.basename(__file__)
softSetupDir = getReg.getRegVal('applicationPath')
appPath = softSetupDir + '\\MainApp.exe'

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def testConfDataBase(self):
        case.confDataBase(softSetupDir,appPath,configList[4])
        username = getpass.getuser()
        xmlList = case.readXml('C:\Users\%s\QuiKLab3\config.xml'%username, 'hostname')
        case.isNotIN('192.168.1.227', xmlList, pyfilename,"192.168.1.227����xml�ļ���")
            
    def tearDown(self):
        pass
#         case.closeLogin(u'��¼--�����Զ����Թ���ϵͳ', u"�˳�")        
        
        
if __name__ == "__main__":
#     pass
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
