# @Author : 杨佳杰
# @Time   : 2022/6/27 10:47
# @File   : 1-pycharm连接mysql.py
from pymysql import *

def main():
    conn=connect(host='192.168.85.128',user='root',password='123',
                 database='python6',charset='utf8')
    # 获取Cursor对象
    cs1=conn.cursor()
    # 增
    count=cs1.execute('insert into calsses(name) values("python3")')
    print(count)
    # 删
    count=cs1.execute('delete from calsses where name="python3"')
    print(count)
    # 更新
    count=cs1.execute('update students set height=178 where height is null')
    print(count)

    conn.commit()# 不加这一条会导致增删改查不会作用到数据库
    cs1.close()
    conn.close()

def main1():
    conn = connect(host='192.168.85.128', user='root', password='123',
                   database='python6', charset='utf8')
    # 获取Cursor对象
    cs1 = conn.cursor()
    # 查询
    count = cs1.execute('select * from students where height<170 and age>18')
    print(count)
    # 获取查询数据
    # 单条获取数据
    # 每个单条数据都是一个元祖
    for i in range(count):
        res=cs1.fetchone()
        print(res)
    cs1.close()
    conn.close()


def main2():
    conn = connect(host='192.168.85.128', user='root', password='123',
                   database='python6', charset='utf8')
    # 获取Cursor对象
    cs1 = conn.cursor()
    # 查询
    count = cs1.execute('select * from students where height<170 and age>18')
    print(count)
    # 获取查询数据
    # 多条获取数据-返回为元祖内嵌多条数据元祖
    res=cs1.fetchmany(3)# 选取少于count数的数据
    print(res)
    cs1.close()
    conn.close()


def main3():
    conn = connect(host='192.168.85.128', user='root', password='123',
                   database='python6', charset='utf8')
    # 获取Cursor对象
    cs1 = conn.cursor()
    # 查询
    count = cs1.execute('select * from students where height<170 and age>18')
    print(count)
    # 获取查询数据
    # 一次性台获取全部数据
    res=cs1.fetchall()
    print(res)
    cs1.close()
    conn.close()


def main4():
    """sql注入示范"""
    conn = connect(host='192.168.85.128', user='root', password='123',
                   database='python6', charset='utf8')
    # 获取Cursor对象
    cs1 = conn.cursor()
    # 查询
    id='1 or 1'
    # 这种拼接方式会导致发生sql注入,即or1导致where条件始终为真,因此输出了表内所有用户信息
    count = cs1.execute(f'select * from students where id={id}')
    print(count)
    # 获取查询数据
    # 一次性台获取全部数据
    res = cs1.fetchall()
    print(res)
    cs1.close()
    conn.close()

def main5():
    """sql注入的防范"-sql语句参数化"""
    conn = connect(host='192.168.85.128', user='root', password='123',
                   database='python6', charset='utf8')
    # 获取Cursor对象
    cs1 = conn.cursor()
    # 查询
    id=[1 or 1]
    # 以列表形式参数化传入,便可以防止sql注入,正常输出id为1的一条数据
    count = cs1.execute('select * from students where id=%s',id)
    # 如果要是有多个参数，需要进行参数化
    # 那么 params = [数值 1, 数值 2....]，此时 sql 语句中有多个%s 即可
    print(count)
    # 获取查询数据
    # 一次性台获取全部数据
    res = cs1.fetchall()
    print(res)
    cs1.close()
    conn.close()

if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    # main3()
    # main4()
    main5()