#Validate Binary Search Tree
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/625/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #in order travers
        if root == None:
            return True
        stack = [root]
        first = True
        while len(stack)>0:
            cur = stack.pop()
            if cur.left:
                stack.append(cur)
                stack.append(cur.left)
                cur.left = None
            else:
                val = cur.val
                if first:
                    prev = val - 1
                    first = False
                if val <= prev:
                    return False
                prev = val
                if cur.right:
                    stack.append(cur.right)
        return True
