# @Author : 杨佳杰
# @Time   : 2022/6/4 11:02
# @File   : 2-引用.py
def test (num):
    print(f'test内num的地址{id(num):x},值为{num}')
    num=5
    print(f'修改后num的地址{id(num):x}')

a=10
print(f'调用前a的地址{id(a):x}')
test(a)
print(f'调用后a的地址{id(a):x}')
print(a)