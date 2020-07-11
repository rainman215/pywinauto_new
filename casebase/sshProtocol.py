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
    
    #上传    
    def upload(self,local_path,target_path):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.put(local_path,target_path)
    
    #下载   
    def download(self,remote_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.get(remote_path,local_path)
        
    #执行命令并将结果打印
    def cmd(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self._transport
        #执行命令
        stdin,stdout,stderr = ssh.exec_command(command,timeout=10)
        #获取命令结果集
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
        
    locScript = path + r'\insAndRunTar.sh'                                  #获取本地脚本位置
    tarScript = r'/home/insAndRunTar.sh'            
    if '0' in ssh.cmd('ls %s;echo $?'%tarScript):                           #下位机脚本不存在则将上位机脚本拷贝到下位机
        print "Script file has exist in target!"
    else:
        ssh.upload(locScript, tarScript)
    srcFile=Install.cpFile('tar')
    print srcFile
    t=srcFile.split('\\')[-1]                                               #获取tar package的名称
    tarFile=r'/home/'+srcFile.split('\\')[-1]                               #指定拷贝到下位机的路径
    if '0' in ssh.cmd('ls %s 2>/dev/null;echo $?'%tarFile):                             #下位机tar包不存在则从上位机拷贝到下位机
        print "Tar file has exist in target!"
    else:
        ssh.upload(srcFile, tarFile)
    ssh.cmd('echo %s >/home/log'%t)
    try:                                                                    #执行下位机安装运行脚本
        ssh.cmd('sh %s 1>&2'%tarScript)
    except:
        ssh.cmd('pidof TargetApp')                                          #获取TargetApp进程ID
    ssh.close()

def tarUsage():
    ssh = SSHConnection(host = '192.168.1.222', port = 22, username = 'root', pwd = 'redhat')
    ssh.connect()
    path = sys.path[0] + r"\casebase"
    if not os.path.exists(path):
        path = os.path.abspath("..") + r"\casebase"

    if not os.path.exists(path):
        path = os.path.abspath("..\..") + r"\casebase"
    locScript = path + r'\get_cpu.sh' #本机脚本路径
    tarScript = r'/home/get_cpu.sh'   #下位机脚本路径
    if '0' in ssh.cmd('ls %s;echo $?'%tarScript):   #下位机是否存在脚本
        print "Script file has exist in target!"
    else:
        ssh.upload(locScript, tarScript)            #上位机脚本拷贝到下位机
    try: 
        ssh.cmd('sh %s 1>&2 &'%tarScript)           #执行下位机脚本
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