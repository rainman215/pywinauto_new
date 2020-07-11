#! /usr/bin/env python
#coding=GB18030
import ConfigParser,sys,os
def readIniConfig(softName):
#     print softName
    readini = ConfigParser.ConfigParser()
    _file = sys.path[0] + r"\data\interfaceConfig.ini"                      #定位interfaceConfig.ini的绝对路径
    if not os.path.exists(_file):                                           
        _file = os.path.abspath("..") + r"\data\interfaceConfig.ini"
    
    if not os.path.exists(_file):
        _file = os.path.abspath("..\..") + r"\data\interfaceConfig.ini" 
    readini.read(_file)                                                     #读取interfaceConfig.ini数据
    section = readini.sections()                                                                
#     print section
    _list=[]
    for sectionInfo in section:                                             #判断sectionInfo数据的参数名是否为空，为空则非法提示错误
        if sectionInfo in softName:
            for key in readini.options(sectionInfo):                
                if readini.get(sectionInfo,key):
                    _list.append(readini.get(sectionInfo,key))
                else:
                    print "Configure file wrong!Please check it."
                    exit()
    if len(_list) == 11:                                                    #根据列表长度与填写的值数目对比判断是否所需配置变量值均都填写
#         print _list
        return _list
    else:
        print 'list length:',len(_list)
        print "Configure file wrong!Please check it."
        exit()
if __name__=='__main__':
    readIniConfig('QuikLab3.0')