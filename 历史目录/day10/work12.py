# @Author : 杨佳杰
# @Time   : 2022/6/10 9:41
# @File   : work12.py
import time
import sys

start_time = time.time()
def prt(lst):
    for item in lst:
        print(item)

if __name__=='__main__':
    prt([1,2,3])#系统传参,输入的一律视为字符串!!
end_time = time.time()
print(time.ctime(end_time))
print(f'程序耗时{(end_time - start_time) * 1000:.1f}ms')
