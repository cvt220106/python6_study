# @Author : 杨佳杰
# @Time   : 2022/6/20 21:17
# @File   : 7-自定义迭代器生成斐波那契.py
class FibInterator:
    def __init__(self, n):
        """
        :param n: 传入所需的斐波那契项数
        """
        self.n = n
        self.current = 0
        self.nums1 = 0  # 斐波那契第一项
        self.nums2 = 1  # 斐波那契第二项

    def __next__(self):
        if self.current < self.n:
            num = self.nums1
            self.nums1, self.nums2 = self.nums2, self.nums1 + self.nums2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    f = FibInterator(10)
    for i in f:
        print(i, end=' ')
