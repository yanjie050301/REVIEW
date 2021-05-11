import re
# a = re.compile(r"h")
# match = a.match("hello world!")
# print(match.group())


a = "ow23ie232323dfj"
b = "23"
# c = re.compile(r".*?{}.*?".format(b))     #正则语句
c = re.compile(r""+b+"")
# f = c.match(a)       #从头开始匹配
f = c.search(a)        #匹配整个字符串
# f = c.findall(a)         #将匹配到的字符以列表的形式显示
print(f.group())

if b in a:
    print("ddddd")











