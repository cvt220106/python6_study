# @Author : 杨佳杰
# @Time   : 2022/6/10 9:52
# @File   : 1-stack.py
class Stack:
    def __init__(self):
        """
        利用列表初始化栈
        """
        self.stack=[]

    def push(self,ele):
        """
        入栈
        :param ele:
        :return:
        """
        self.stack.append(ele)

    def pop(self):
        """
        出栈
        :return:
        """
        self.stack.pop()

    def top(self):
        """
        获取栈顶元素
        :return:
        """
        if self.empty():
            return 'stack is empty!'
        return self.stack[-1]

    def isempty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.stack==[]#为空则返回True

    def size(self):
        """
        获取栈的深度
        :return:
        """
        return len(self.stack)

if __name__=='__main__':
    s=Stack()
    print(s.isempty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.size())
    print(s.stack)
    s.pop()
    s.pop()
    print(s.stack)
