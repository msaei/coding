#Subsets
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

#Lexicographic (Binary Sorted) Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            
        return ans


# Recursive solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

# Backtracking solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
