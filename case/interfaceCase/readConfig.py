#! /usr/bin/env python
#coding=GB18030
import ConfigParser,sys,os
def readIniConfig(softName):
#     print softName
    readini = ConfigParser.ConfigParser()
    _file = sys.path[0] + r"\data\interfaceConfig.ini"                      #��λinterfaceConfig.ini�ľ���·��
    if not os.path.exists(_file):                                           
        _file = os.path.abspath("..") + r"\data\interfaceConfig.ini"
    
    if not os.path.exists(_file):
        _file = os.path.abspath("..\..") + r"\data\interfaceConfig.ini" 
    readini.read(_file)                                                     #��ȡinterfaceConfig.ini����
    section = readini.sections()                                                                
#     print section
    _list=[]
    for sectionInfo in section:                                             #�ж�sectionInfo���ݵĲ������Ƿ�Ϊ�գ�Ϊ����Ƿ���ʾ����
        if sectionInfo in softName:
            for key in readini.options(sectionInfo):                
                if readini.get(sectionInfo,key):
                    _list.append(readini.get(sectionInfo,key))
                else:
                    print "Configure file wrong!Please check it."
                    exit()
    if len(_list) == 11:                                                    #�����б�������д��ֵ��Ŀ�Ա��ж��Ƿ��������ñ���ֵ������д
#         print _list
        return _list
    else:
        print 'list length:',len(_list)
        print "Configure file wrong!Please check it."
        exit()
if __name__=='__main__':
    readIniConfig('QuikLab3.0')