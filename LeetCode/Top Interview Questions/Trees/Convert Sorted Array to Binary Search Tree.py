#Convert Sorted Array to Binary Search Tree
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/631/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        mid = n // 2
        leftNums = nums[:mid]
        rightNums = nums[mid+1:]
        middle = nums[mid]
        root = TreeNode(middle)
        root.left = self.sortedArrayToBST(leftNums)
        root.right = self.sortedArrayToBST(rightNums)
        return root
