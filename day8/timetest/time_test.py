import time
print(time.time())     #时间戳
print(time.localtime())     #time.struct_time(tm_year=2021, tm_mon=3, tm_mday=6, tm_hour=10, tm_min=57, tm_sec=12,)
print(time.strftime("%Y_%m_%d-%H-%M-%S",time.localtime()))    #格式化时间输出，定义输出的时间的形式





















