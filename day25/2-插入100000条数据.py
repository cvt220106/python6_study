# @Author : 杨佳杰
# @Time   : 2022/6/27 16:29
# @File   : 2-插入100000条数据.py
from pymysql import *

def main():
    conn=connect(host='192.168.85.128',user='root',password='123',
                 database='jing_dong',charset='utf8')

    cs1=conn.cursor()
    for i in range(100000):
        cs1.execute("insert into test_index values('ha-%d')" % i)

    conn.commit()

if __name__ == '__main__':
    main()