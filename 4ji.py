# encoding = utf-8
from sws_mysql import sws_mysql
from sws_get import *
import re

## 插入四级词汇到数据库
def insert():
    mysql = sws_mysql("root","7829558","vocabulary")
    db = mysql.db
    cursor = mysql.cursor
    fo = open("data/1.txt","r+",encoding='utf-8')
    txt = fo.read()
    # 正则匹配
    find = object
    index = 0
    while True:
        pattern = re.compile(r'\b([a-z|A-Z]+)\b')
        find = pattern.search(txt,index)
        if find==None:
            break
        index = find.span()[1]
        name = find.groups()[0]
        print(name)
        #插入数据库
        sql0 = "select * from 4ji where name = '" + name + "'"
        try:
            cursor.execute(sql0)
            data = cursor.fetchone()
            if data == None:
                sql = "insert into 4ji(name) values('"+ name +"')"
                try: 
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                    print("error:",find)
        except:
            print("error")


def is4ji():
    mysql = sws_mysql("root","7829558","vocabulary")
    db = mysql.db
    cursor = mysql.cursor
    sql = "select (name) from words"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name = row[0]
        sql = "select (name) from 4ji where name = '" + name +"'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if(result!=None):
            sql = "update words set is4ji = 1 where name = '" + name +"'"
            cursor.execute(sql)
            db.commit()
    mysql.close()
is4ji()