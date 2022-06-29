import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择: '))
        if choice in range(8):
            if choice == 0:
                answer = input('您确定要退出系统吗?y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用!')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('=====================学生管理系统========================')
    print('----------------------------功能菜单---------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.学生信息排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('--------------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('请输入id（如：1001）：')
        if not id:
            break
        name = input('请输入学生姓名：')
        if not name:
            break
        # 利用tey...except...结构来防止输入非整数成绩
        try:
            math = int(input('请输入该生的数学成绩：'))
            english = int(input('请输入该生英语成绩：'))
            python = int(input('请输入该生的python成绩：'))
        except:
            print('输入的成绩不是整数类型，请重新输入！')
            continue
        # 将录入的学生信息逸字典形式进行保存
        student = {'id': id, 'name': name, 'math': math, 'english': english, 'python': python}
        # 将学生信息保存至列表中
        student_list.append(student)
        answer = input('是否继续添加?y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    save(student_list)
    print('学生信息录入成功!!')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查询请输入1,按姓名请输入2：')
            if mode == '1':
                id = input('请输入需要查询的学生id：')
            elif mode == '2':
                name = input('请输入要查询的学生姓名：')
            else:
                print('您的输入有误，请重新输入！！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
                for item in student_old:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询的学生的信息
            show_student(student_query)
            # 清空查询列表
            student_query.clear()
            answer = input('是否继续查询？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('系统内暂未保存学生信息！')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^8}\t{:^8}\t{:8}\t{:^8}\t{:^8}'
    print(format_title.format('ID', '姓名', '数学成绩', '英语成绩', 'python成绩', '总成绩'))
    format_data = '{:^6}\t{:^8}\t{:^8}\t{:8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item['id'],
                                 item['name'],
                                 item['math'],
                                 item['english'],
                                 item['python'],
                                 int(item['math']) + int(item['english']) + int(item['python'])))


def delete():
    while True:
        student_id = input('请输入要删除的学生id：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as nfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            nfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'学号为{student_id}的学生信息已删除!')
                    else:
                        print(f'没有找到学号为{student_id}的学生信息!')
            else:
                print('系统内无学生信息!')
                break
            show()  # 删除完成后显示当前系统内的学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    student_id = input('请输入要修改的学生id：')
    with open(filename, 'w', encoding='utf-8') as nfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print(f'找到学号为{student_id}的学生信息,可以开始修改了')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['math'] = int(input('请输入数学成绩：'))
                        d['english'] = int(input('请输入英语成绩：'))
                        d['python'] = int(input('请输入python成绩：'))
                    except:
                        print('您的输入有误，请重新输入!！')
                    else:
                        break
                nfile.write(str(d) + '\n')
                print(f'学生id为{student_id}的学生信息修改成功!!')
            else:
                nfile.write(str(d) + '\n')
    answer = input('是否继续修改?y/n\n')
    if answer == 'y' or answer == 'Y':
        modify()  # 再次调用该函数


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
        student_new = []
        for item in student:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择（0，升序，1.降序）：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入错误，请重新输入！！')
        sort()
    sort_mode = input('请选择排序方式（1.按数学成绩排序，2.按英语成绩排序，3.按python成绩排序,0.按总成绩排序）：')
    if sort_mode == '1':
        student_new.sort(key=lambda x: int(x['math']), reverse=asc_or_desc_bool)
    elif sort_mode == '2':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif sort_mode == '3':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif sort_mode == '0':
        student_new.sort(key=lambda x: int(x['math']) + int(x['english']) + int(x['python']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print(f'学生系统内共有{len(student)}名学生！')
            else:
                print('系统内暂未录入学生信息！！')
    else:
        print('暂未保存学生信息！！')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存学生信息！！')


if __name__ == '__main__':
    main()
