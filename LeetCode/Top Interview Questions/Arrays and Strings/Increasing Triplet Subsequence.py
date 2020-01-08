#Increasing Triplet Subsequence
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums or len(nums)<3:
            return False
        
        min1=nums[0]
        min2=float('inf')
        
        for i in range(1,len(nums)):
            if nums[i]<min1:
                min1=nums[i]
            elif nums[i]>min1 and nums[i]<min2:
                min2=nums[i]
            elif nums[i]>min2:
                return True
        return False
