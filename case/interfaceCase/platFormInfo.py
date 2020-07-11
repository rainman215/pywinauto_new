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

a='\x00' #C�����еĿո�
configList = readConfig.readIniConfig('QuikLab3.0')
regInfo = regInfo.getRegVal('applicationPath')
# print regInfo
os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")

class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        assert lib.initQuiKLabPlatform() == 0,'��ʼ��ʧ�ܣ�\n'                 
        time.sleep(5)
        assert lib.loadProject(configList[4]) == 0,'���ع���ʧ�ܣ�\n'

    @classmethod
    def tearDown(self):
        assert lib.releaseQuiKLabPlatform() == 0,'�����ͷ�ʧ�ܣ�\n'

    def testName_platFormInfo(self):
        targetIp = cardName = cardInfo = 't'*1024
        tarIpCount=lib.getTargetCount()
#         print tarIpCount
        assert tarIpCount > 0,'��ȡ��λ��ʧ�ܣ�\n'
        for i in range(tarIpCount):                                             #������ȡ��λ��IP
            assert lib.getTargetIP(i,targetIp,1024) == 0,'��ȡ��λ��IPʧ�ܣ�\n'
#             print targetIp
            assert lib.getIpState(targetIp) == 1,'��λ��%s�����ߣ�\n'%targetIp
            print '��λ��%s����!\n'%targetIp.strip(a)
            assert lib.updateInterfInfos() == 0,'����Ӳ����Դ��Ϣʧ�ܣ�\n'
            cardNum = lib.getInterfNumFromIp(targetIp.strip(a))
#             print '��λ��IP:'+targetIp.strip(a)
            print '�忨����:',cardNum
            Ip=targetIp.strip(a)
            for i in range(cardNum):                                            #������ȡ��λ���忨��Ϣ
                assert lib.getInterfInfo(Ip,i,cardName,1024,cardInfo,1024) == 0,'��ȡ�忨��Ϣʧ�ܣ�\n'
                print "**********��%s��忨:**********"%(i+1)
                print "�忨����:"+cardName.strip(a)
                print "�忨��Ϣ:"+cardInfo.strip(a)
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     sys.stdout=logger.Logger('2.txt')
    unittest.main()