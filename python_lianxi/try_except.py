"""
练习一个try和两个except结合捕获异常
"""
try:
    a = int(input("请输入内容："))
    # print(bdb)
# except ValueError as e:
#     print(f"具体异常：{e}")
except Exception as e:

    raise ValueError("a 必须是数字")
    print("2222222")
