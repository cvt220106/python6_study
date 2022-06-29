# @Author : 杨佳杰
# @Time   : 2022/6/3 20:23
# @File   : work3.py
# 使用input()读取变量,练习print的各种变量类型输出

name=input('情输入姓名:')
student_no=int(input('请输入学号:'))
gpa=float(input('请输入绩点:'))
# %格式化输出
print('学生%4s的年龄是%06d,绩点是%.2f'%(name,student_no,gpa))
# format格式化输出
print('学生{0}的年龄是{1:06d},绩点是{2:.2f}'.format(name,student_no,gpa))
# fstring格式化输出
print(f'学生{name}的年龄是{student_no:06d},绩点是{gpa:.2f}')
