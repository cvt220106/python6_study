# @Author : 杨佳杰
# @Time   : 2022/6/28 21:51
# @File   : work1.py
def line(k,b):
    def calc_y(x):
        print(k*x+b)
    return calc_y


line_1=line(1,2)
# y=x+2
line_1(0)
line_1(1)
line_2=line(2,1)
# y-=2x+1
line_2(0)
line_2(1)