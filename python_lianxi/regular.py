import re
a = re.compile(r"h")
match = a.match("hello world!")
# print(match.group())



b = "tid="26119"></span></div>\n\t\t\t\t\t\t\t\t\t<div class="todo_detail todoDetail">\n\t\t\t\t\t\t\t\t\t\t<h4><a class="edit" tid="26119" ttype="1" tdate="2021-03-31" tstatus="0">ceshi1111</a></h4>\n\t\t\t\t\t\t\t\t\t\t<p><span class="tcontent">ddddd</span></p>\n\t\t\t\t\t\t\t\t\t</div"
f = re.search(r"ceshi1111",b)
print(f.group())

















