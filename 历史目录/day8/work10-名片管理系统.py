# @Author : 杨佳杰
# @Time   : 2022/6/7 23:24
# @File   : work10-名片管理系统.py
import os
filename='card.txt'


def main():#程序启动
    while True:
        menu()
        choice = int(input('请选择: '))
        if choice in range(4):
            if choice==0:
                answer = input('您确定要退出系统吗?y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用!')
                    break  # 退出系统
                else:
                    continue
            elif choice==1:
                create_new()
            elif choice==2:
                show_all()
            elif choice==3:
                search()
        else:
            print('输入错误，请重新输入！')


def menu():
    """菜单"""
    print('*'*50)
    print('欢迎使用【名片管理系统】V1.0\n')
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片\n')
    print('0.退出系统')
    print('*'*50)


def create_new():
    """新建名片"""
    card_list=[]
    while True:
        name=input('请输入姓名:')
        tele_num=input('请输入电话:')
        qq_num=input('请输入qq号:')
        email=input('请输入邮箱:')
        card={'姓名':name,'电话':tele_num,'QQ':qq_num,'email':email}
        card_list.append(card)
        answer = input('是否继续新建?y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(card_list)#将名片存进内存文件
    print('新建名片成功!!')


def save(lst):
    try:#文件存在则追加,不存在则创建并写入
        card_txt = open(filename, 'a', encoding='utf-8')
    except:
        card_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:#遍历名片列表,逐个名片的写入文件
        card_txt.write(str(item) + '\n')
    card_txt.close()


def show_all():
    """显示全部"""
    card_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            card = rfile.readlines()
            for item in card:
                card_lst.append(eval(item))
            if card_lst:
                show_card(card_lst)
    else:
        print('暂未保存学生信息！！')


def show_card(lst):
    if len(lst) == 0:
        print('没有名片信息，无数据显示！！')
        return
    # 定义标题显示格式t
    format_title = '{:^8}\t{:^5}\t{:^6}\t\t{:16}'
    print(format_title.format('姓名', '电话', 'QQ', 'email'))
    format_data = '{:^8}\t{:^6}\t{:^6}\t{:16}'
    for item in lst:
        print(format_data.format(item['姓名'],
                                 item['电话'],
                                 item['QQ'],
                                 item['email']))


def search():
    """查找名片"""
    card_query = []
    while True:
        name = ''
        if os.path.exists(filename):
            name = input('请输入要查询的学生姓名：')
            with open(filename, 'r', encoding='utf-8') as rfile:
                card_old = rfile.readlines()
                for item in card_old:
                    d = dict(eval(item))
                    if d['姓名'] == name:
                        card_query.append(d)
            # 显示查询的学生的信息
            show_card(card_query)
            # 清空查询列表
            card_query.clear()
            answer = input('是否继续查询？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('系统内暂未保存学生信息！')
            return

if __name__=='__main__':
    main()