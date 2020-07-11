#! /usr/bin/env python
#coding=GB18030
import ctypes
import json
import os
import sys
import time
import unittest

from case.interfaceCase import readConfig
import casebase.getReg as regInfo
import data
# import logger
# logFile = sys.argv[0].split('\\')[-1].replace('py','txt')
# print logFile
# sys.stderr=logger.Logger(logFile)

a='\x00' #C语言中的空格
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# print regInfo
os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")

class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        assert lib.initQuiKLabPlatform() == 0,'初始化失败！\n'                 
        time.sleep(5)
        assert lib.loadProject(configList[4]) == 0,'加载工程失败！\n'

    @classmethod
    def tearDown(self):
        assert lib.releaseQuiKLabPlatform() == 0,'工程释放失败！\n'

    def testName_platFormInfo(self):
        targetIp = cardName = cardInfo = 't'*1024
        tarIpCount=lib.getTargetCount()
#         print tarIpCount
        assert tarIpCount > 0,'获取下位机失败！\n'
        for i in range(tarIpCount):                                             #遍历获取下位机IP
            assert lib.getTargetIP(i,targetIp,1024) == 0,'获取下位机IP失败！\n'
#             print targetIp
            assert lib.getIpState(targetIp) == 1,'下位机%s不在线！\n'%targetIp
            print '下位机%s在线!\n'%targetIp.strip(a)
            assert lib.updateInterfInfos() == 0,'更新硬件资源信息失败！\n'
            cardNum = lib.getInterfNumFromIp(targetIp.strip(a))
#             print '下位机IP:'+targetIp.strip(a)
            print '板卡个数:',cardNum
            Ip=targetIp.strip(a)
            for i in range(cardNum):                                            #遍历获取下位机板卡信息
                assert lib.getInterfInfo(Ip,i,cardName,1024,cardInfo,1024) == 0,'获取板卡信息失败！\n'
                print "**********第%s块板卡:**********"%(i+1)
                print "板卡名称:"+cardName.strip(a)
                print "板卡信息:"+cardInfo.strip(a)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     sys.stdout=logger.Logger('2.txt')
    unittest.main()