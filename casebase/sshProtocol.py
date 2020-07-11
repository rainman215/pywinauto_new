#!/usr/bin/env python
#coding=GB18030
import os
import sys
import uuid

import paramiko
import dirLocation
import casebase.QuikLab_Install as Install
from _socket import timeout


class SSHConnection(object):
    def __init__(self, host, port, username, pwd):
        
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self._k = None
        
    def connect(self):
        transport = paramiko.Transport(self.host,self.port)
        transport.connect(username = self.username, password = self.pwd)
        self._transport = transport
        
    def close(self):
        self._transport.close()
    
    #�ϴ�    
    def upload(self,local_path,target_path):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.put(local_path,target_path)
    
    #����   
    def download(self,remote_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.get(remote_path,local_path)
        
    #ִ������������ӡ
    def cmd(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self._transport
        #ִ������
        stdin,stdout,stderr = ssh.exec_command(command,timeout=10)
        #��ȡ��������
        result = stderr.read()
        print str(result)
        return result

def insTar():
#     import pdb;pdb.set_trace()
    ssh = SSHConnection(host = '192.168.1.222', port = 22, username = 'root', pwd = 'redhat')
    ssh.connect()
#     path = sys.path[0] + r"\casebase"
#     if not os.path.exists(path):
#         path = os.path.abspath("..") + r"\casebase"
# 
#     if not os.path.exists(path):
#         path = os.path.abspath("..\..") + r"\casebase"
    path=dirLocation.searchDir('casebase')
        
    locScript = path + r'\insAndRunTar.sh'                                  #��ȡ���ؽű�λ��
    tarScript = r'/home/insAndRunTar.sh'            
    if '0' in ssh.cmd('ls %s;echo $?'%tarScript):                           #��λ���ű�����������λ���ű���������λ��
        print "Script file has exist in target!"
    else:
        ssh.upload(locScript, tarScript)
    srcFile=Install.cpFile('tar')
    print srcFile
    t=srcFile.split('\\')[-1]                                               #��ȡtar package������
    tarFile=r'/home/'+srcFile.split('\\')[-1]                               #ָ����������λ����·��
    if '0' in ssh.cmd('ls %s 2>/dev/null;echo $?'%tarFile):                             #��λ��tar�������������λ����������λ��
        print "Tar file has exist in target!"
    else:
        ssh.upload(srcFile, tarFile)
    ssh.cmd('echo %s >/home/log'%t)
    try:                                                                    #ִ����λ����װ���нű�
        ssh.cmd('sh %s 1>&2'%tarScript)
    except:
        ssh.cmd('pidof TargetApp')                                          #��ȡTargetApp����ID
    ssh.close()

def tarUsage():
    ssh = SSHConnection(host = '192.168.1.222', port = 22, username = 'root', pwd = 'redhat')
    ssh.connect()
    path = sys.path[0] + r"\casebase"
    if not os.path.exists(path):
        path = os.path.abspath("..") + r"\casebase"

    if not os.path.exists(path):
        path = os.path.abspath("..\..") + r"\casebase"
    locScript = path + r'\get_cpu.sh' #�����ű�·��
    tarScript = r'/home/get_cpu.sh'   #��λ���ű�·��
    if '0' in ssh.cmd('ls %s;echo $?'%tarScript):   #��λ���Ƿ���ڽű�
        print "Script file has exist in target!"
    else:
        ssh.upload(locScript, tarScript)            #��λ���ű���������λ��
    try: 
        ssh.cmd('sh %s 1>&2 &'%tarScript)           #ִ����λ���ű�
    except:
        pass
    ssh.close()
if __name__=='__main__':
    insTar()
#     tarUsage()
#     ssh = SSHConnection(host = '192.168.1.222', port = 22, username = 'root', pwd = 'redhat')
#     ssh.connect()
#     if '0' in ssh.cmd('ls /home/insAndRunTar.sh;echo $?'):
#         print "wrong"
# #     ssh.cmd("ls")
#     srcFile=Install.cpFile('tar')
#     print srcFile
#     t=srcFile.split('\\')[-1]
#     tarFile=r'/home/'+srcFile.split('\\')[-1]
# #     ssh.cmd('echo %s >/home/log'%t)
#     ssh.upload(srcFile, tarFile)
#     ssh.cmd('kill -9 `pidof TargetApp`')
#     ssh.cmd('tar -zxvf %s'%tarFile)
#     try:
#     ssh.cmd('sh /home/get_cpu.sh')
#     except:
#         pass
#     ssh.cmd('sh /home/install.sh')
#     ssh.cmd('ls /home/123')
#     ssh.cmd('echo $?')

# ssh.download('/tmp/ks77.py', 'sl.py')
#     ssh.cmd('pidof TargetApp')

#     import casebase.QuikLab_Install as Install
#     Install.cpFile('tar')
#     ssh.close()