#! /usr/bin/env python
#coding=GB18030
import _winreg
#获取注册表QuikLab安装目录(applicationPath)和工作空间地址(workspace)
def getRegVal(para):
    key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Keliang\QuiKLab") #注册表软件键路径
    try:
        i=0
        while 1:                                                #遍历注册表键值
            name,value,type=_winreg.EnumValue(key,i)
    #         print repr(name),
            i+=1
    except WindowsError:
        value,type = _winreg.QueryValueEx(key,para)
        return(value)                                           #返回注册表键值
if __name__ == '__main__':
    print getRegVal("applicationPath")                          
    print getRegVal("workSpace")