from sws_mysql import sws_mysql
from sws_get import *
import re
mysql = sws_mysql("root","7829558","vocabulary")

##part1
##
# fo = open("data/Twilight.txt","r+")
# txt = fo.read()

# # 正则匹配
# find = object
# index = 0
# # i = 20
# while True:
#     pattern = re.compile(r'\b([a-z|A-Z]+)\b')
#     find = pattern.search(txt,index)
#     if find==None:
#         break
#     index = find.span()[1]
#     #插入数据库
#     mysql.insertWord(find.group())
#     # i -= 1
#     # if i<=0:
#     #     break

##part2
##
results = mysql.selectword()
for row in results:
    tr = searchword(row[1])
    mysql.insertTr(row[1],tr)
    n = row[0]
    if(n%10 == 0):
        print("已爬取%d个单词的含义" % n)

mysql.close()