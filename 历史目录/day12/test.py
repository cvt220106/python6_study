nums1 = [1, 3]
nums2 = [2]
m = len(nums1)
n = len(nums2)
nums = [0] * (m + n)
i, j, k = 0, 0, 0
while i < m or j < n:
    if j == n:
        nums[k] = nums1[i]
        i += 1
    elif i == m:
        nums[k] = nums2[j]
        j += 1
    elif nums1[i] <= nums2[j]:
        nums[k] = nums1[i]
        i += 1
    else:
        nums[k] = nums2[j]
        j += 1
    k += 1
print(nums)
mid = (m + n) // 2
if (m + n) % 2 == 0:
    print((nums[mid] + nums[mid - 1]) / 2)
else:
    print(float(nums[mid]))
