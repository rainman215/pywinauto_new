#! /usr/bin/env python
#coding=GB18030
import _winreg
#��ȡע���QuikLab��װĿ¼(applicationPath)�͹����ռ��ַ(workspace)
def getRegVal(para):
    key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Keliang\QuiKLab") #ע��������·��
    try:
        i=0
        while 1:                                                #����ע����ֵ
            name,value,type=_winreg.EnumValue(key,i)
    #         print repr(name),
            i+=1
    except WindowsError:
        value,type = _winreg.QueryValueEx(key,para)
        return(value)                                           #����ע����ֵ
if __name__ == '__main__':
    print getRegVal("applicationPath")                          
    print getRegVal("workSpace")