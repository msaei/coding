#Remove Duplicates from Sorted Array
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        i = 1
        previous = nums[0]
        while i < len(nums):
            if nums[i] == previous:
                nums.pop(i)
            else:
                previous = nums[i]
                i += 1
        return len(nums)
