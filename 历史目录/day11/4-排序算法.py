# @Author : 杨佳杰
# @Time   : 2022/6/10 15:11
# @File   : 4-排序算法.py
import random


class MySort:
    def __init__(self, n, num_range):
        self.n = n  # 元素个数
        self.num_range = num_range
        self.arr = [random.randint(0, num_range) for i in range(n)]

    def bubble_sort(self, reverse=False):
        """
        冒泡排序
        :param reverse:
        :return:
        """
        i = self.n - 1
        arr = self.arr
        while i > 0:
            j = 0
            if reverse:  # 降序
                while j < i:
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
            else:  # 升序
                while j < i:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
            i -= 1

    def select_sort(self, reverse=False):
        """
        选择排序
        :param reverse:
        :return:
        """
        arr = self.arr
        i = 0
        while i < self.n - 1:
            m_pos = i  # 最大或最小的元素下标标记
            j = i + 1
            if reverse:  # 降序,每轮找最大数
                while j < self.n:
                    if arr[j] > arr[m_pos]:
                        m_pos = j
                    j += 1
            else:  # 升序,每轮找最小数
                while j < self.n:
                    if arr[j] < arr[m_pos]:
                        m_pos = j
                    j += 1
            arr[i], arr[m_pos] = arr[m_pos], arr[i]
            i += 1

    def insert_sort(self, reverse=False):
        """
        插入排序
        :param reverse:
        :return:
        """
        arr = self.arr
        i = 1
        while i < self.n:
            insert_value = arr[i]
            j = i - 1
            if reverse:  # 降序
                while j >= 0:
                    if insert_value > arr[j]:
                        arr[j + 1] = arr[j]
                    else:
                        break
                    j -= 1
            else:  # 升序
                while j >= 0:
                    if insert_value < arr[j]:
                        arr[j + 1] = arr[j]
                    else:
                        break
                    j -= 1
            arr[j + 1] = insert_value
            i += 1

    def shell_sort(self, reverse=False):
        arr = self.arr
        gap = self.n >> 1
        while gap > 0:
            i = gap
            while i < self.n:
                insert_value = arr[i]
                j = i - gap
                if reverse:  # 降序
                    while j >= 0:
                        if insert_value > arr[j]:
                            arr[j + gap] = arr[j]
                        else:
                            break
                        j -= gap
                else:  # 升序
                    while j >= 0:
                        if insert_value < arr[j]:
                            arr[j + gap] = arr[j]
                        else:
                            break
                        j -= gap
                arr[j + gap] = insert_value
                i += 1
            gap = gap >> 1

    def partition(self, left, right):
        """
        分割函数，找到分割点的下标值
        :param left:
        :param right:
        :return:
        """
        arr = self.arr
        k = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        """
        快速排序
        :param left:
        :param right:
        :return:
        """
        if left < right:
            arr = self.arr
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def big_heap_adjust(self,pos,len):
        """
        调整堆内某棵子树为大根堆
        :param pos: 子树的父节点
        :param len: 堆内元素个数
        :return:
        """
        arr=self.arr
        dad=pos
        son=2*dad+1#左孩子
        while son<len:#存在孩子节点时，持续调整
            if son+1<len and arr[son+1]>arr[son]:
                son+=1#右孩子存在时，比拼两个孩子的大小，找出更大值
            if arr[son]>arr[dad]:
                arr[son],arr[dad]=arr[dad],arr[son]
                dad=son
                son=2*dad+1
            else:
                break

    def heap_sort(self):
        """
        堆排序，建大根堆
        :return:
        """
        arr=self.arr
        for i in range(self.n//2-1,-1,-1):#调整整个序列为大根堆,堆顶为最大元素
            self.big_heap_adjust(i,self.n)
        arr[0],arr[self.n-1]=arr[self.n-1],arr[0]#将堆顶元素放至堆尾，从新调整堆
        for i in range(self.n-1,1,-1):
            self.big_heap_adjust(0,i)#后续调整时只需调整堆顶为0的子树
            #每次调整都能得到一个未排序序列的最大值，然后将最大值放到未排序序列的尾
            arr[0],arr[i-1]=arr[i-1],arr[0]

    def test_sort(self, sort_method, *args, **kwargs):
        print(self.arr)
        sort_method(*args, **kwargs)
        print(self.arr)

if __name__ == '__main__':
    s = MySort(10, 99)
    #s.test_sort(s.quick_sort,0,s.n-1)  # 升序
    s.test_sort(s.heap_sort)
