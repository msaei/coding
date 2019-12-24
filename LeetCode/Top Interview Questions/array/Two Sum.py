#Two Sum
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numDic.keys():
                return (numDic[complement], i)
            numDic[nums[i]] = i
        return None
