review1 = "    accumulate over A long period     "
# 1.查找某字符，结合范围，两种方法，述说不同点
# print(review1.find("A"))
# print(review1.index("b"))    #index查找没有符合的字符会报错，find不会报错
# 2.统计某字符在字符串中出现的次数，结合范围，
# print(review1.count("a"))
# print(review1.count("v",2,10))
# 3.替换字符串这种的某字符，结合替换次数
# print(review1.replace("c","D",1))
# 4.分割字符串，结合分割次数
# print(review1.split("a",1))
# 5.用一个字符或子串合并字符串
# print("_".join(review1))
# 6.某字符串第一个字母转化为大写
# print(review1.capitalize())
# 7.将字符串每个单词首字母转换成大写
# print(review1.title())
# 8.将字符串中的大写转换成小写。
# print(review1.lower())
# 9.将字符串中小写转成大写
# print(review1.upper())
# 10.删除字符串左侧空白字符
# print(review1.lstrip())
# 11.删除字符串右侧空白字符
# print(review1.rstrip())
# 12.删除字符串两侧空白字符
# print(review1.strip())
# 13.判断该字符串是否以“Accumulate”开头
# print(review1.startswith(" "))
# 14.判断该字符串是否以“period”结尾
# print(review1.endswith(" "))
review2 = "keep"
# 15.将keep左对齐，用*填充到12个字符
# print(review2.ljust(12,"*"))
# 16.将keep右对齐，用*填充到12个字符
# print(review2.rjust(12,"*"))
# 17.将keep居中显示，用*填充到12个字符
# print(review2.center(12,"*"))
review3 = "456464565464"
review4 = "sfhksh465jfd"
review5 = "    "
# 18.判断字符串review4是否是纯字母
print(review4.isalpha())
# 19判断字符串review3是否是纯数字
print(review3.isdigit())
# 20.判断字符串review4是否是数字和字母组成
print(review4.isalnum())
# 21.判断字符串review3是否是只包含空格
print(review5.isspace())