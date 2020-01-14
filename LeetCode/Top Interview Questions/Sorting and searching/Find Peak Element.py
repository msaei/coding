#Find Peak Element
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l-1):
            if nums[i+1] < nums[i]:
                return i
        return l - 1
