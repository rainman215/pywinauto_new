#! /usr/bin/env python
#coding=GB18030
import os
import re


def getRev(type):
    path='\\\\192.168.1.226\\���԰汾\\PC14421'                    #ָ���汾���°汾·��
    filelist=os.listdir(path)                   #��ȡָ��Ŀ¼�������ļ�����
    _list=[]
    for t in filelist:
        p=r'\d\.0\.0\.\d*'
        m=re.findall(p,t)                                       #��ȡ���а汾��
        if m:
            ver=m[0].split('.')[-1]                             
            _list.append(ver)                                   ##����ȡ���а汾�Ŵ���_list������
    for t in filelist:                                          #��ѯĿ¼�������ļ�
        if max(_list) in t:                                     #��_list���ֵ�ڸ��ļ���
            if type == 'exe':                                       #��׺Ϊexeʱ
                if t.split('.')[-1] == 'exe':                   #��ȡ����exe�汾��
                    srcFile=path+'\\'+t
                    return(srcFile)
            elif type == 'tar':                                 #��׺Ϊtarʱ
                if t.split('.')[-1] == 'tar':                   #��ȡ����tar�汾��
                    srcFile=path+'\\'+t
                    return(srcFile)
if __name__ == '__main__':
    print getRev('tar')