# @Author : 杨佳杰
# @Time   : 2022/6/10 10:16
# @File   : 2-队列.py
from collections import deque#双端队列
def use_deque():
    queue = deque(["Eric", "John", "Michael"])
    queue.append('luke')
    print(queue)
    print(queue.popleft())
    print(queue)
    queue[0] = 'xiongda'
    print(queue[0])

class CalcQueue:#循环队列
    def __init__(self,size:int):
        self.size=size
        self.arr=[None]*size
        self.front=0
        self.rear=0

    def isfull(self):
        """
        判断循环队列是否已满
        :return:
        """
        return (self.rear+1)%self.size==self.front

    def isempty(self):
        """
        判断循环队列是否为空
        :return:
        """
        return self.rear==self.front

    def enqueue(self,elem):
        """
        入队操作
        :param elem:
        :return:
        """
        if self.isfull():
            print('队列已满!入队失败!')
            return False
        self.arr[self.rear]=elem
        self.rear=(self.rear+1)%self.size
        return True

    def dequeue(self):
        """
        出队操作,同时返回出队元素
        :return:
        """
        if self.isempty():
            print('队列为空!出队失败!')
            return
        res=self.arr[self.front]
        self.arr[self.front]=None
        self.front=(self.front+1)%self.size
        return res

    def __str__(self):
        return str(self.arr)

if __name__=='__main__':
    #use_deque()
    cqueue=CalcQueue(5)
    print(cqueue.isempty())
    print(cqueue.isfull())
    cqueue.enqueue(1)
    print(cqueue)
    cqueue.enqueue(2)
    print(cqueue)
    cqueue.enqueue(3)
    print(cqueue)
    cqueue.enqueue(4)
    print(cqueue)
    print(cqueue.isfull())
    cqueue.enqueue(5)
    print(cqueue.dequeue())
    print(cqueue)
    cqueue.enqueue(5)
    print(cqueue)
    cqueue.enqueue(6)



