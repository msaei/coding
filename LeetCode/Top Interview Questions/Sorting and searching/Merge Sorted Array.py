#Merge Sorted Array
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/587/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        i1 = 0
        i2 = 0
        j = 0
        while j<len(nums1):
            if i1 >= m:
                nums1[j] = nums2[i2]
                i2 += 1
            elif i2 >= n:
                nums1[j] = temp[i1]
                i1 += 1
            elif temp[i1] < nums2[i2]:
                nums1[j] = temp[i1]
                i1 += 1
            else:
                nums1[j] = nums2[i2]
                i2 += 1
            j += 1
