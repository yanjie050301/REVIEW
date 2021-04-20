import unittest

from ddt import ddt,data

from  python_lianxi.register import register

@ddt
class RegisterTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")

    def setUp(self):
        print("每条测试用例开始")
    cases=[
        {"title": "注册成功",  'expected': {"code": 1, "msg": "注册成功"},'data':["limiyou","123456",'123456']},
        {"title": "密码不一致", 'expected': {"code": 0, "msg": "两次密码不一致"}, 'data': ("miyoua", "12345", '123456')},
        {"title": "账户已存在", 'expected': {"code": 0, "msg": "该账户已存在"}, 'data': ("lemontree", "123456", '123456')},
    ]
    @data(*cases)
    def test_register(self,case):
        try:
            a = register(*case['data'])
            # print(a)
            self.assertEqual(case['expected'],a.re(),msg="用例失败")
        except Exception as msg:
            print(msg)
        else:
            print("ceshichengg ")
    def tearDown(self):
        print("每条测试用例结束")
    @classmethod
    def tearDownClass(cls):
        print("测试结束")
if __name__ == "__main__":
    unittest.main()




# cases = {"title": "注册成功",  'expected': {"code": 1, "msg": "注册成功"},'data':("limiyou","123456",'123456')}
# a =cases["data"]
# print(a)















"""

# 1、一行代码实现1--100之和
# 利用sum()函数求和
print(sum(i for i in range(1,101)))

print(int((1+100)*100/2))



2、如何在一个函数内部修改全局变量

利用global 修改全局变量



3、列出5个python标准库

os：提供了不少与操作系统相关联的函数

sys:   通常用于命令行参数

re:   正则匹配

math: 数学运算

datetime:处理日期时间
"""


# 4、字典如何删除键和合并两个字典
# d = {"a":1,"b":2}
# b = {"c":3}
# 删除字典元素
# del d["a"]
# 删除字典
# del b
#合并两个字典
# b.update(d)
# print(b)

"""
5、谈下python的GIL

GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。
所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

 

6、python实现列表去重的方法

 




7、fun(*args,**kwargs)中的*args,**kwargs什么意思？



8、python2和python3的range（100）的区别

9、一句话解释什么样的语言能够用装饰器?


10、python内建数据类型有哪些


 

11、简述面向对象中__new__和__init__区别

 



12、简述with方法打开处理文件帮我我们做了什么？

 

13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]




14、python中生成随机整数、随机小数、0--1之间小数方法




 

15、避免转义给字符串加哪个字母表示原始字符串？

 

16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的



17、python中断言方法举例




20、python2和python3区别？列举5个

1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')


 

21、列出python中可变数据类型和不可变数据类型，并简述原理

 




 

22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

 




 

23、用lambda函数实现两个数相乘

 



24、字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}



25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"



26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"



27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



29、正则re.complie作用


30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？




31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
32、用python删除文件和用linux命令删除文件方法
33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
36、写一段自定义异常代码
37、正则表达式匹配中，（.*）和（.*?）匹配区别？
39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
41、举例说明异常模块中try except else finally的相关意义
42、python中交换两个数值
43、举例说明zip（）函数用法
44、a="张明 98分"，用re.sub，将98替换为100
46、a="hello"和b="你好"编码成bytes类型
47、[1,2,3]+[4,5,6]的结果是多少？
52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
53、写一个单列模式
54、保留两位小数
58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
66、python中copy和deepcopy区别
69、请将[i for i in range(3)]改成生成器
70、a = "  hehheh  ",去除收尾空格
77、根据键对字典排序（方法一，zip函数）
78、根据键对字典排序（方法二,不用zip)
82、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
83、正则匹配以163.com结尾的邮箱
84、递归求和
85、python字典和json字符串相互转化方法
87、统计字符串中某字符出现次数
88、字符串转化大小写
89、用两种方法去空格
90、正则匹配不是以4和7结尾的手机号
97、r、r+、rb、rb+文件打开模式区别
99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
100、python传参数是传值还是传址？

"""