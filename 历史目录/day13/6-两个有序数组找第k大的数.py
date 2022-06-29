# @Author : 杨佳杰
# @Time   : 2022/6/14 0:08
# @File   : 6-两个有序数组找第k大的数.py
def getKthElement(nums1: list[int], nums2: list[int], k: int):
    """
    m=len(nums1),n=len(nums2)
    - 主要思路：要找到第 k (k>1) 大的元素，那么就取 pivot1 = nums1[m-k/2] 和 pivot2 = nums2[n-k/2] 进行比较
    - 这里的 "/" 表示整除
    - nums1 中大于等于 pivot1 的元素有 nums1[m-k/2..m-1] 共计 k/2-1 个
    - nums2 中大于等于 pivot2 的元素有 nums2[n-k/2..n-1] 共计 k/2-1 个
    - 取 pivot = max(pivot1, pivot2)，两个数组中大于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
    - 这样 pivot 本身最大也只能是第 k-1 小的元素
    - 如果 pivot = pivot1，那么 nums1[m-k/2..m-1] 都不可能是第 k 大的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
    - 如果 pivot = pivot2，那么 nums2[n-k/2..n-1] 都不可能是第 k 大的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
    - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
    """
    m, n = len(nums1), len(nums2)
    index1, index2 = m - 1, n - 1
    while True:
        # 特殊情况
        if index1 == 0:
            return nums2[index2 + k - 1]
        if index2 == 0:
            return nums1[index1 + k - 1]
        if k == 1:
            return max(nums1[index1], nums2[index2])
        # 正常情况
        newIndex1 = max(index1 - k // 2 + 1, 0)
        newIndex2 = max(index2 - k // 2 + 1, 0)
        pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
        if pivot1 >= pivot2:
            k -= index1 - newIndex1 + 1
            index1 = newIndex1 - 1
        else:
            k -= index2 - newIndex2 + 1
            index2 = newIndex2 - 1

def main(k):
    array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17]
    array2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 29]
    print(getKthElement(array1,array2,k))

if __name__=='__main__':
    main(4)
