#3sum
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums)<3:
            return res

        nums.sort()
        for i in range(len(nums)):

            if nums[i]>0:
                break
            elif i>0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i + 1;
                right = len(nums) - 1
                while(left<right):
                    temp = nums[i] + nums[left]+ nums[right]
                    if  temp == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        while (left<right and nums[left]==nums[left+1]):
                            left = left + 1
                        while (left<right and nums[right]==nums[right-1]):
                            right = right - 1
                        left = left + 1
                        right = right - 1
                    elif    temp<0:
                        left = left + 1
                    elif    temp>0:
                        right = right - 1

        return res
