#! /usr/bin/env python
#coding=GB18030
import json
import re
import casebase.case_wrapper as case
import pymysql
configList = case.readIniConfig('QuikLab3.0')

class check(object):
    def __init__(self):
        self.db = pymysql.connect(host = configList[8],port = int(configList[9]),user = configList[11],passwd = configList[12],db = configList[10],charset = 'utf8')
    #�ж����ݿ����Ƿ���ڸ��û�
    def ckUname(self,uName):
        cur = self.db.cursor()
        cmmd='SELECT Name FROM mydb.tbl_user;'      #Sql�����ѯ�û���
        cur.execute(cmmd)                               
        data = cur.fetchall()                       #�������ݿ�����������data
        for i in range(0,len(data)):                #������ѯ�Ľ��
#             print data
            if uName == data[i][0]:                 #�ҵ��û����򷵻�1
                print "find user"
                cur.close()
                return(1)
        cur.close()
        print "No user"
        return (0)        
    #�ж����ݿ����Ƿ���ڸù�������
    def ckProName(self,proName):
        cur = self.db.cursor()
        cmd = 'SELECT Name FROM mydb.tbl_resources where name="' + proName + '"'   #Sql�����ѯ������
        cur.execute(cmd)
        data = cur.fetchall()               #�������ݿ�����������data
        cur.close()
        if len(data) == 0:                  #����ѯ�������Ƴ���Ϊ0����û�в鵽��������������0
            print "No Project Name!"
            return (0)
        else:                               #��ѯ���������Ȳ�Ϊ0�������ҵ�������������1
            print "Project Exist!"
            return (1)
        
        
#ƥ�����ݿ��Ƿ���ڸù��̣����������1���ݹ�ƥ��ֱ���������ݿⲻ���ڵĹ�����
#     def getProName(self,proName):
#         cur = self.db.cursor()
#         cur.execute('SELECT Name FROM mydb.tbl_resources where type=6;')
#         data = cur.fetchall()
#         for i in range(0,len(data)):
#             a=json.dumps(data[i][0],encoding='utf-8',ensure_ascii=False).strip('"').encode('GB18030')
# #             print proName,a
#             if proName == a:
# #                 print proName,a
#                 flag=proName[-1]
#                 if re.match('\d', flag):
#                     flag=int(flag)+1
#                     proName=proName[0:-1]+str(flag)
#                 else:                    
#                     proName=proName+'1'
# #                     print proName,a
# #                     print data[i][0].decode('utf-8').encode('GB18030')
# #                     if proName == a:
# #                         print 'equal'
# #                     else:
# #                         print 'not equal'
# #                 print type(proName)
#                 self.getProName(proName)
#         cur.close()
#         return proName
#     
    
    def getProName(self,proName):
        while True:
            cur = self.db.cursor()
            cmd = 'SELECT Name FROM mydb.tbl_resources where name="' + proName + '"'    #Sql�����ѯ������
            cur.execute(cmd)
            data = cur.fetchall()
            cur.close()
            if len(data) == 0:                  #�����ҹ���������Ϊ0(û�鵽)���˳�ѭ��
#                 print data,type(data)
                return(proName)
                break
            else:                               #�����ҵ�������
                flag=proName[-1]                #��ȡ���������һλ
                if re.match('\d', flag):        #�ж��Ƿ�Ϊ����
                    flag=int(flag)+1            #Ϊ������+1
                    proName=proName[0:-1]+str(flag) #������ɹ�����
                else:                    
                    proName=proName+'1'         #��Ϊ�����򹤳���ֱ��+'1'
if __name__=='__main__':
    p=check()
    print p.getProName('cl_pro1')
