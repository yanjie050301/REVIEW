import re
# a = re.compile(r"h")
# match = a.match("hello world!")
# print(match.group())


a = "ow23ie232323dfj"
b = "23"
# c = re.compile(r".*?{}.*?".format(b))
c = re.compile(r".*?"+b+"")
f = c.search(a)
print(f.group())

















