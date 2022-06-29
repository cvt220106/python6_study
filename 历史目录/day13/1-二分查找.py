# @Author : 杨佳杰
# @Time   : 2022/6/13 10:14
# @File   : 1-二分查找.py
def binary_search(arr: list[int], target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 查找失败


if __name__ == '__main__':
    list1 = [4, 8, 10, 32, 43, 45, 76, 87, 91]
    print(binary_search(list1, 87), list1.index(87), lis)
