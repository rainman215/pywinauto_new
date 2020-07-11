#! /usr/bin/env python
#coding=utf-8
import json
import re
import sys

import pymysql


reload(sys)
sys.setdefaultencoding('utf8')

def unicToList(Name,patt):
    i=json.dumps(Name,encoding='utf-8',ensure_ascii=False).strip('"').encode('utf8')       #使用jason将Name编码成utf8
    Name=re.findall(patt,i)                                                                 #匹配Name中需要的关键字
#     print Name
    return(Name)

def unicToList2(Name,patt):
    i=json.dumps(Name,encoding='utf-8',ensure_ascii=False).strip('"')                   #使用jason将Name编码
    Name=re.findall(patt,i)
#     print Name
    return(Name)

class check(object):
    def __init__(self):
        self.db = pymysql.connect(host = '192.168.1.226',port = 3306,user = 'root',passwd = 'root',db = 'mydb',charset = 'utf8')
    
    def search(self,cmmd):
        cur = self.db.cursor()
        cur.execute(cmmd)
        data = cur.fetchall()
        cur.close()
        return(data)
    
    '''
             查询工程下的ID 
            条件：1、根据tbl_resources中的工程名称查询工程ID
    '''
    def getProName(self):
        cur = self.db.cursor()
        proSql ='SELECT Name FROM mydb.tbl_resources where type=6;'         #从工程命中查找Name
        cur.execute(proSql)
        proName = cur.fetchall()
        proName = list(proName)
        for i in range(len(proName)):                                   #按照数据库查到所有工程名个数遍历
            proName[i] = proName[i][0]                                  
        proName = repr(proName).decode('unicode_escape')                #编解码处理
#         for i in proName:
#             proName = proName.replace('u','')
        cur.close()
        patt=r"\'(.*?)\'"
        proName=unicToList2(proName,patt)                               #调用编解码处理函数
#         print proName
        return(proName)
     
    '''
             查询工程下的用例分类名称
            条件：1、根据tbl_resources中的工程ID
        2、tbl_resources表中‘Testcase’的ID作为父ID
    '''
    def getTestCaseClassName(self,proName):
        cur = self.db.cursor()
        testCaseClassSql = '''select Name From mydb.tbl_resources 
                            where parentId=(select id From mydb.tbl_resources 
                            where parentId=(select id FROM mydb.tbl_resources where Name="'''+proName+'''") and name='Testcase');'''
        cur.execute(testCaseClassSql)
        testCaseClass = cur.fetchall()
        testCaseClass = list(testCaseClass)
        for i in range(len(testCaseClass)):
            testCaseClass[i] = testCaseClass[i][0]
        testCaseClass = repr(testCaseClass).decode('unicode_escape')
#         for i in testCaseClass:
#             testCaseClass = testCaseClass.replace('u','')    
        cur.close()

        patt=r"\'(.*?)\'"
        testCaseClass=unicToList2(testCaseClass,patt)
        return(testCaseClass)
    
    
    '''
            查询工程用例分类下用例名称
           条件：1、tbl_resources中工程ID
        2、tbl_resources父ID在工程下用例分类的ID中
        3、tbl_resources中父ID在测试用例分类名字的ID中
    '''
    def getTestCaseName(self,proName,testCaseClassName):
        cur = self.db.cursor()
        testCaseSql = '''select Name from  mydb.tbl_resources 
                        where parentId= (select id From mydb.tbl_resources 
                        where parentId=(select id From mydb.tbl_resources 
                        where parentId=(select id FROM mydb.tbl_resources 
                        where Name="'''+proName+'''") and name='Testcase') and Name="'''+testCaseClassName+'''");'''
        cur.execute(testCaseSql)
        testCase = cur.fetchall()
        testCase = list(testCase)
        for i in range(len(testCase)):
            testCase[i] = testCase[i][0]
        testCase = repr(testCase).decode('unicode_escape')
#         for i in testCase:
#             testCase = testCase.replace('u','')    
        cur.close()

        patt=r"\'(.*?)\'"
        testCase=unicToList(testCase,patt)
#         print testCase
        return(testCase) 

    '''
            查询工程下任务分类名称
            条件：1、根据tbl_resources中的工程ID
        2、tbl_resources表中‘TestTask’的ID作为父ID
    '''
    def getTestTaskClassName(self,proName):
        cur = self.db.cursor()
        testTaskClassSql = '''SELECT Name FROM mydb.tbl_resources 
                            where parentId= (SELECT id FROM mydb.tbl_resources 
                            where parentId= (select id FROM mydb.tbl_resources 
                            where Name="'''+proName+'''") and Name = 'TestTask');'''
        cur.execute(testTaskClassSql)
        testTaskClass = cur.fetchall()
        testTaskClass = list(testTaskClass)
        for i in range(len(testTaskClass)):
            testTaskClass[i] = testTaskClass[i][0]
        testTaskClass = repr(testTaskClass).decode('unicode_escape')
        cur.close()

        patt=r"\'(.*?)\'"
        testTaskClass=unicToList(testTaskClass,patt)
        return(testTaskClass)
    '''
            查询工程下任务分类下的任务名称
            条件：1、tbl_resources中工程ID
        2、tbl_resources父ID在工程下任务分类的ID中
        3、tbl_resourcesID在测试任务分类名字的ID中
    '''
    def getTestTaskName(self,proName,testTaskClassName):
        cur = self.db.cursor()
        testTaskSql = '''SELECT Name FROM mydb.tbl_resources 
                        where parentId= (SELECT id FROM mydb.tbl_resources 
                        where parentId= (SELECT id FROM mydb.tbl_resources 
                        where parentId= (select id FROM mydb.tbl_resources 
                        where Name="'''+proName+'''") and Name = 'TestTask') and Name="'''+testTaskClassName+'''");'''
        cur.execute(testTaskSql)
        testTask = cur.fetchall()
        testTask = list(testTask)
        for i in range(len(testTask)):
            testTask[i] = testTask[i][0]
        testTask = repr(testTask).decode('unicode_escape')
        cur.close()
#         i=json.dumps(testTask,encoding='utf-8',ensure_ascii=False).strip('"').encode('utf8')
        patt=r"\'(.*?)\'"
        testTask=unicToList(testTask,patt)
        return(testTask)

    '''
            查询工程测试任务下的测试用例
            条件：1、tbl_resources中工程ID
        2、tbl_resources父ID在工程下任务分类的ID中
        3、tbl_resources中父ID在测试任务分类名字的ID中
        4、tbl_resourcescontentindex中的resourcecontentid与tbl_resources中的任务ID相等
        5、tbl_resourcescontent中的Id与tbl_resourcescontentindex中的TestTask.xml ID相等
    '''
    def getTestTaskTestCaseInfo(self,proName,testTaskClassName,testTaskName):
        cur = self.db.cursor()
        testTaskTestCaseSql =  '''SELECT resourcevalue FROM mydb.tbl_resourcescontent 
                                where id = (SELECT resourcecontentid FROM mydb.tbl_resourcescontentindex 
                                where resourceid= (SELECT id FROM mydb.tbl_resources 
                                where parentId= (SELECT id FROM mydb.tbl_resources 
                                where parentId= (SELECT id FROM mydb.tbl_resources 
                                where parentId= (select id FROM mydb.tbl_resources 
                                where Name="'''+proName+'''") and Name = 'TestTask') and Name="'''+testTaskClassName+'''") and name="'''+testTaskName+'''") and resourcekey='TestTask.xml');'''                       
#         print testTaskTestCaseSql
        cur.execute(testTaskTestCaseSql)
        testTaskTestCase = cur.fetchall()
        testTaskTestCase = list(testTaskTestCase)
        for i in range(len(testTaskTestCase)):
            testTaskTestCase[i] = testTaskTestCase[i][0]
        testTaskTestCase = repr(testTaskTestCase).decode('unicode_escape')
        cur.close()
        patt=r"\'(.*?)\'"
        testTaskTestCase=unicToList(testTaskTestCase,patt)
        testTaskTestCase =  re.sub('\\\\n*','',testTaskTestCase[0]).replace('GBK','utf-8')
        return(testTaskTestCase)

    '''
            查询工程下的信号信息
           条件：1、tbl_resources表中工程ID
        2、tbl_resourcescontentindex中resourceid与tbl_resources表中工程ID相等
        3、tbl_resourcescontent中id与tbl_resourcescontentindex中resourcecontentid相等
        4、resourceKey = 'SystemEnv'的resourcevalue字段的值
    ''' 
    def getSignalInfo(self,proName): 
        cur = self.db.cursor()
        signalInfoSql =  '''select resourcevalue from mydb.tbl_resources a left join mydb.tbl_resourcescontentindex b on a.id = b.resourceid left join mydb.tbl_resourcescontent c on b.resourcecontentid = c.id 
                            where name = "''' +  proName + '''"and b.resourceKey = 'SystemEnv';'''  
        
#         print signalInfoSql                   
        cur.execute(signalInfoSql)
        signalInfo = cur.fetchall()
        signalInfo = list(signalInfo)
        for i in range(len(signalInfo)):
            signalInfo[i] = signalInfo[i][0] 
        signalInfo = repr(signalInfo).decode('unicode_escape') 
#         print signalInfo
        cur.close()
        patt=r"\'(.*?)\'"
        signalInfo = unicToList(signalInfo,patt)
        signalInfo =  re.sub('\\\\n*','',signalInfo[0]).replace('GBK','utf-8')
#         print signalInfo
#         dom = test.lxmlReader(signalInfo)
#         print dom.getTabQualityValue("//Signals/Routing/@name")
#         print type(dom.getTabQualityValue("//Signals/Routing/@name"))
#         print dom.getTabQualityValue("//to/text()")
        return(signalInfo)
    
    def getFileResources(self,proName):
        cur = self.db.cursor()
        FRInfo= '''SELECT * FROM mydb.tbl_resources 
                where parentId = (SELECT id FROM mydb.tbl_resources 
                where parentId=(SELECT id FROM mydb.tbl_resources 
                where name="''' + proName + '''") and name='other')'''
        cur.execute(FRInfo)
        FRInfo= cur.fetchall()
        FRInfo = list(FRInfo)
        for i in range(len(FRInfo)):
            FRInfo[i] = FRInfo[i][3] 
        FRInfo = repr(FRInfo).decode('unicode_escape') 
#         print FRInfo
        cur.close()
        patt=r"\'(.*?)\'"
        FRInfo=unicToList(FRInfo,patt)
        return(FRInfo)
    
if __name__=='__main__':
    p=check()
#     print p.getProName()
#     for i in p.getProName():
#         print i
#     for i in p.getTestCaseClassName('1111'):
#         print i
    print p.getTestCaseName('cl_pro','用例分类')
#     for i in p.getTestTaskClassName('1111'):
#         print i
#     for i in p.getTestTaskName('1111','45'):
#         print i
#     for i in p.getTestTaskTestCaseName('1111','45','ww'):
#         print i
#     print type(p.getTestCaseClassName('cl_pro')[0])

