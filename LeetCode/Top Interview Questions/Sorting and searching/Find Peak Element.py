#Find Peak Element
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/

class Solution:
    #binary search ln(n), 1
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while(l<r):
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

    #linear scan n, 1
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l-1):
            if nums[i+1] < nums[i]:
                return i
        return l - 1
