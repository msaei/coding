#Intersection of Two Arrays II
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        res = []
        for n in nums1:
            if n in hashMap.keys():
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        for n in nums2:
            if n in hashMap.keys() and hashMap[n] > 0:
                res.append(n)
                hashMap[n] -= 1
        return res
