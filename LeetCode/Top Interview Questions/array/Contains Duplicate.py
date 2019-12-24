#Contains Duplicate
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if n in dic.keys():
                return True
            dic[n] = 1
        return False
