#Move Zeroes
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail = []
        i = 0
        while i < len(nums):
            if nums[i] == 0 :
                nums.pop(i)
                tail.append(0)
                continue
            i += 1
        nums += tail
