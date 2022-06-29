# @Author : 杨佳杰
# @Time   : 2022/6/4 20:18
# @File   : work3.py
# 写一个模块（命名不要用中文），模块里写3个打印函数
# 然后另外一个py文件调用该模块，并调用对应模块的函数，同时用一下下面操作
import def_print

if __name__ == '__main__':
    nm='yang'
    city='Zhengzhou'
    def_print.print_star()
    def_print.print_info(nm,city)
    def_print.print_thanks(3)