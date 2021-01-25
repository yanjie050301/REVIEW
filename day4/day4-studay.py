# _*_ conding:utf-8 _*_
"""
#定义一个类
class Washer():
    #创建一个方法
    #定义初始化功能的函数
    def __init__(self,width,height):
        #添加实例属性
        self.width = width
        self.height = height
    def print_info(self):
        #类里面获取实例属性
        print(f"haier1的宽度是：{self.width}")
        print(f"haier1洗衣机的高度是：{self.height}")
    def wash(self):
        print("我会洗衣服")
        # print(self)
    # def __str__(self):
    #     return "jintianlianxipython"
    def __del__(self):
        print(f"{self}对象已经被删除")
#创建对象    实例化
haier1 = Washer(10,30)
# print(haier1)         #打印对象在内存中的地址
print(haier1)            #若加上__str__方法，则打印return的数据
haier1.wash()
# haier2 = Washer()      #只要创建对象，就会开辟新的地址
# print(haier2)
# haier1.width = 300
# haier1.height = 800
print()
haier1.print_info()
# print(f"haier1的宽度是：{haier1.width}")
# print(f"haier1洗衣机的高度是：{haier1.height}")
del haier1
"""
#继承
"""
class A():
    def __init__(self):
        self.num = 1
    def info_num(self):
        print(self.num)
class B(A):
    pass
result = B()
result.info_num()
"""
"""
#单继承
class Master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class Perntice(Master):
    pass
xiaoming = Perntice()
xiaoming.make_cake()
"""
#多继承
"""
class Master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class School():
    def __init__(self):
        self.kongfu = "[香辣的煎饼果子]"
    def make_cake(self):
        print("运用{self.kongfu}制作香辣煎饼果子")
class Perntice(School,Master):               #同一个方式的时候，调用第一个父类的方法
    pass
xiaoming = Perntice()
print(xiaoming.kongfu)
xiaoming.make_cake()
"""
#⼦类重写⽗类同名⽅法和属性，子类独自创造方法
"""
class Master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class School():
    def __init__(self):
        self.kongfu = "[香辣的煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作香辣煎饼果子")
class Perntice(School,Master):            #拥有自己的方法
    def __init__(self):
        self.kongfu = "[独创的煎饼果子]"
    def make_cake(self):
        #如果先调用父类的属性和方法，父类的属性方法会覆盖子类的属性方法，故先调用子类的初始化方法
        self.__init__()
        print(f"运用{self.kongfu}制作独创煎饼果子")
    def make_master_cake(self):
        #调用父类的方法，为了保证调用的是父类的属性，故先调用父类的初始化方法
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
xiaoming = Perntice()
print(xiaoming.kongfu)
xiaoming.make_cake()
xiaoming.make_master_cake()
xiaoming.make_school_cake()
"""
#多层继承
"""
class Master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class School():
    def __init__(self):
        self.kongfu = "[香辣的煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作香辣煎饼果子")
class Perntice(School,Master):            #拥有自己的方法
    def __init__(self):
        self.kongfu = "[独创的煎饼果子]"
    def make_cake(self):
        #如果先调用父类的属性和方法，父类的属性方法会覆盖子类的属性方法，故先调用子类的初始化方法
        self.__init__()
        print(f"运用{self.kongfu}制作独创煎饼果子")
    def make_master_cake(self):
        #调用父类的方法，为了保证调用的是父类的属性，故先调用父类的初始化方法
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
#创建了一个xiaoming的徒弟类，要继承xiaoming***********************
class Tysyn(Perntice):
    pass
xiaoming = Perntice()
print(xiaoming.kongfu)
xiaoming.make_cake()
xiaoming.make_master_cake()
xiaoming.make_school_cake()

xiaogang = Tysyn()
xiaogang.make_cake()
xiaogang.make_school_cake()
"""
#super方法,优点：简化代码，若父类名字被修改，不用修改下面的代码
# 师傅类
"""
class Master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
# 学校继承老师傅类
class School(Master):
    def __init__(self):
        self.kongfu = "[香辣的煎饼果子]"
    def make_cake1(self):
        print(f"运用{self.kongfu}制作香辣煎饼果子")
    def make_cake2(self):
        #super()就是父类的意思
        super().__init__()
        super().make_cake()
#学校有学生
class Student(School):
    def __init__(self):
        self.kongfu = "[独创的煎饼果子]"
    def make_cake(self):
        # 如果先调用父类的属性和方法，父类的属性方法会覆盖子类的属性方法，故先调用子类的初始化方法
        self.__init__()
        print(f"运用{self.kongfu}制作独创煎饼果子")
    def make_old_cake1(self):
        super().__init__()
        super().make_cake()
scho = School()
# scho.make_cake1()
scho.make_cake2()

xiaoping = Student()
#只能调用父类，不能调用父类的父类
xiaoping.make_old_cake1()
"""
#############私有权限
"""
class Master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class School():
    def __init__(self):
        self.kongfu = "[香辣的煎饼果子]"
    def make_cake(self):
        print("运用{self.kongfu}制作香辣煎饼果子")
class Perntice(School,Master):

    def __init__(self):
        self.kongfu = "[独创的煎饼果子]"
        #定义私有属性
        self.__monkey = 1000
    #定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__monkey)
    def make_cake(self):
        self.__init__()
        print(f"运用{self.kongfu}制作独创煎饼果子")


xiaoming = Perntice()
print(xiaoming.kongfu)
xiaoming.make_cake()
"""

