import pymysql
class sws_mysql(object):
    user = ''
    password = ''
    database = ''
    table = 'words'
    db = object
    cursor = object
    def __init__(self,user,password,database):
        self.user = user
        self.password = password
        self.database = database
        try:
            #打开数据库链接
            self.db = pymysql.connect(host="localhost",
                                    user=self.user,
                                    password=self.password,
                                    db=self.database,
                                    charset='utf8',)
            #创建游标
            self.cursor = self.db.cursor()
            print("数据库链接成功!")
        except:
            print("error:数据库链接失败!")
    ##插入单词
    #如果单词已存在数据库则次数加1
    def insertWord(self,word):
        db = self.db
        cursor = self.cursor
        sql = "select * from " + self.table + " where name = '" + word + "'"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if(result==None):
                #查询失败，将单词增加到数据库内
                sql2 = "insert into " + self.table + "(name,num) values('" + word +"','1')"
                try:
                    cursor.execute(sql2)
                    db.commit()
                except:
                    db.rollback()
                    print(sql2)
                    print("error:'%s'添加至数据库失败！" % word)
            #查询成功，次数加一
            sql1 = "update " + self.table +" set num = num + 1 where name = '" + word + "'"
            try:
                cursor.execute(sql1)
                #print(sql1)
                db.commit()
            except:
                db.rollback()
                print("error:'%s'更新次数失败！" % word)
        except:
            print("error")
    
    #查询单词
    def selectword(self):
        db = self.db
        cursor = self.cursor
        sql = "select * from " + self.table + " where translation = ''"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except:
            print('error')
    #更新单词含义
    def insertTr(self,name,translation):
        db = self.db
        cursor = self.cursor
        sql = "update " + self.table +" set translation = '" + translation + "' where name = '" + name + "'"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            print("error:'%s'更新含义失败！" % name)
    #关闭数据库
    def close(self):
        self.db.close()
        print("数据库已关闭！")
