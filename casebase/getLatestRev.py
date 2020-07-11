#! /usr/bin/env python
#coding=GB18030
import os
import re


def getRev(type):
    path='\\\\192.168.1.226\\测试版本\\PC14421'                    #指定版本最新版本路径
    filelist=os.listdir(path)                   #获取指定目录下所有文件名称
    _list=[]
    for t in filelist:
        p=r'\d\.0\.0\.\d*'
        m=re.findall(p,t)                                       #获取所有版本号
        if m:
            ver=m[0].split('.')[-1]                             
            _list.append(ver)                                   ##将获取所有版本号存入_list数组内
    for t in filelist:                                          #轮询目录下所有文件
        if max(_list) in t:                                     #若_list最大值在该文件中
            if type == 'exe':                                       #后缀为exe时
                if t.split('.')[-1] == 'exe':                   #获取最新exe版本号
                    srcFile=path+'\\'+t
                    return(srcFile)
            elif type == 'tar':                                 #后缀为tar时
                if t.split('.')[-1] == 'tar':                   #获取最新tar版本号
                    srcFile=path+'\\'+t
                    return(srcFile)
if __name__ == '__main__':
    print getRev('tar')