#Permutations
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        
        def backtrack(ns: List[int], perm: List[int]):
            if len(ns) == 0:
                ans.append(perm)
                return
            for i in range(len(ns)):
                d = ns[i]
                nns = ns[:i] + ns[(i+1):]
                backtrack(nns, [d] + perm[:])
                
        backtrack(nums, [])
        return ans
