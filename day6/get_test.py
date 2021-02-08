import requests


# # 1.请求地址
# urlstr = "https://wanandroid.com/"
# # 2.发送请求
# r = requests.get(url = urlstr)
# #3.输出响应结果
# print(r.status_code)
# print(r.text)

# 1.请求地址
url = "https://www.baidu.com/"
# 2.发送请求
r = requests.get(url = url)
# 3.输出响应数据
print(r.status_code)     #打印状态码
# print(r.text)            #打印字符串方式的响应体响应体
print(r.apparent_encoding)
print(r.encoding)

