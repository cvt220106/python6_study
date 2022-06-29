# @Author : 杨佳杰
# @Time   : 2022/6/20 21:13
# @File   : test.py
def test():
    list1.append(3)
    print(list1)


if __name__ == '__main__':
    list1 = [1, 2]
    print(id(list1))
    test()
    print(list1)
