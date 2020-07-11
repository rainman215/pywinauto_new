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
    #判断数据库内是否存在该用户
    def ckUname(self,uName):
        cur = self.db.cursor()
        cmmd='SELECT Name FROM mydb.tbl_user;'      #Sql命令查询用户名
        cur.execute(cmmd)                               
        data = cur.fetchall()                       #根据数据库命令将结果传给data
        for i in range(0,len(data)):                #遍历查询的结果
#             print data
            if uName == data[i][0]:                 #找到用户名则返回1
                print "find user"
                cur.close()
                return(1)
        cur.close()
        print "No user"
        return (0)        
    #判断数据库内是否存在该工程名称
    def ckProName(self,proName):
        cur = self.db.cursor()
        cmd = 'SELECT Name FROM mydb.tbl_resources where name="' + proName + '"'   #Sql命令查询工程名
        cur.execute(cmd)
        data = cur.fetchall()               #根据数据库命令将结果传给data
        cur.close()
        if len(data) == 0:                  #若查询工程名称长度为0，即没有查到工程名，并返回0
            print "No Project Name!"
            return (0)
        else:                               #查询工程名长度不为0，即查找到工程名，返回1
            print "Project Exist!"
            return (1)
        
        
#匹配数据库是否存在该工程，若存在则加1并递归匹配直到生成数据库不存在的工程名
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
            cmd = 'SELECT Name FROM mydb.tbl_resources where name="' + proName + '"'    #Sql命令查询工程名
            cur.execute(cmd)
            data = cur.fetchall()
            cur.close()
            if len(data) == 0:                  #若查找工程名长度为0(没查到)，退出循环
#                 print data,type(data)
                return(proName)
                break
            else:                               #若查找到工程名
                flag=proName[-1]                #获取工程名最后一位
                if re.match('\d', flag):        #判断是否为数字
                    flag=int(flag)+1            #为数字则+1
                    proName=proName[0:-1]+str(flag) #重新组成工程名
                else:                    
                    proName=proName+'1'         #不为数字则工程名直接+'1'
if __name__=='__main__':
    p=check()
    print p.getProName('cl_pro1')
