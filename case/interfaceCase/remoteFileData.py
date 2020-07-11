#! /usr/bin/env python
#coding=utf-8
import ctypes
import os
import casebase.getReg as regInfo


regInfo = regInfo.getRegVal('applicationPath')
os.chdir(regInfo)
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")

class remoteFileData(object):
    def __init__(self):
        self.path='\\\\192.168.1.226\Users\Administrator\QuiKLab3\Resources'
        
    def getProName(self):
        ProNameList = []
        proDir = self.path + '\Projects'
        Profilelist=os.listdir(proDir)
        for ProFile in Profilelist:
            if os.path.isdir(os.path.join(proDir,ProFile)) and ProFile != '__public_library_resource__':
                ProNameList.append(ProFile)
        return ProNameList
                
                
               
if __name__=='__main__':
    p=remoteFileData()
    print p.getProName()
    
    