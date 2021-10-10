import os
import sqlite3
import urllib
import matplotlib.pyplot as plt


# windows下，chrome浏览历史记录默认路径
# os.path.expanduser(str path) 把path中的~替换为user目录
path = os.path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default\History"
print(path)
# 连接数据库
connection = sqlite3.connect(path)
# connection = sqlite3.connect(r"D:\Desktop\History")
# 执行sql，得到游标（游标是一种能从包括多条数据记录的结果集中每次提取一条记录的机制）
cursor = connection.execute('select url from urls')
# 存储网址-次数的字典
dict_website = {}
# 遍历游标的每一行
for row in cursor:
    # 调用urllib库的urlparse方法，解析url得到网址
    # urlparse返回的是一个ParseResult类型的对象，它包含6部分，分别是scheme（协议）、netloc（域名）、path、params、query和fragment
    # 不用urllib库的话，可利用正则表达式取到域名
    website = urllib.parse.urlparse(row[0]).netloc
    # 获得网站出现的频次
    # setdefault(key[, default])
    # If key is in the dictionary, return its value.
    # If not, insert key with a value of default and return default. default defaults to None.
    count = dict_website.setdefault(website, 0)
    # 更新网址的频次
    dict_website[website] = count + 1
# 按照频次排序
# sorted(iterable, cmp=None, key=None, reverse=False)
# items() 返字典的(键, 值)元组的列表。
list_website = sorted(dict_website.items(), key=lambda x: x[1], reverse=True)
for x in list_website:
    print(x)
# 用matplotlib库绘制饼图
plt.pie(x=[x[1] for x in list_website[:20]], labels=[x[0] for x in list_website[:20]], autopct='%1.2f%%', normalize=True)
plt.show()