import urllib.request
import re

def searchword(word):
    url = "http://www.youdao.com/w/eng/"+ word +"/#keyfrom=dict2.index"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    try:
        data = data.decode('utf-8')
    except:
        print("error:未能解码网页内容：",data)
        data = ""
        exit()

    #找到所有含义
    pattern = re.compile(r'<div class="trans-container">([\s\S]*?)</div>')
    try:
        match = pattern.search(data)
        data = match.group()
    except:
        data = ""
        print("error:%s含义未爬取成功" % word)
    # print(data)
    #存储含义
    wordstr = ""
    index = 0
    while True:
        pattern = re.compile(r'<li>(.*?)</li>')
        match = pattern.search(data,index)
        if match==None:
            break
        index = match.span()[1]
        wordstr +=match.groups()[0] + "  "
    return wordstr
