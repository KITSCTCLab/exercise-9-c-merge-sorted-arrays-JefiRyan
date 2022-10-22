from typing import List




def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = j = k = 0
    l_arr = nums1[:m]
    r_arr = nums2[:n]
    while j < len(l_arr) and k < len(r_arr):
        if l_arr[j] < r_arr[k]:
            nums1[i] = l_arr[j]
            j += 1
        else:
            nums1[i] = r_arr[k]
            k += 1
        i += 1

    while j < len(l_arr):
        nums1[i] = l_arr[j]
        i += 1
        j += 1

    while k < len(r_arr):
        nums1[i] = r_arr[k]
        i += 1
        k += 1

    return nums1


# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
