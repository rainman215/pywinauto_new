#! /usr/bin/env python
#coding=GB18030
import pymysql
# db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',passwd = '1234',db = 'quikta',charset = 'utf8')
def checkName(proName):
    db = pymysql.connect(host = '192.168.1.226',port = 3306,user = 'root',passwd = 'root',db = 'mydb',charset = 'utf8')
    cur = db.cursor()
    cur.execute('SELECT Name FROM mydb.tbl_project;')
    data = cur.fetchall()
    # print data
    for i in range(0,len(data)):
        if data[i][0] == proName:
            print "find user"
            cur.close()
            return (1)
        else:
            cur.close()
            return (0)
if __name__=='__main__':
    print checkName('709')
    