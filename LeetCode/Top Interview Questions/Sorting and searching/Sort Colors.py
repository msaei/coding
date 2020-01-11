#Sort Colors
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = -1
        i2 = len(nums)
        i = 0
        while i < i2:
            if nums[i] == 0:
                i0+= 1
                nums[i], nums[i0] = nums[i0], nums[i]
                if i == i0:
                    i+=1
            elif nums[i] == 2:
                i2 -= 1
                nums[i], nums[i2] = nums[i2], nums[i]
            else:
                i += 1
        return
