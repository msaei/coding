#Symmetric Tree
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/627/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # level traverse
        # put each level values including none to an array
        # compare array with its reverse
        if root == None:
            return True
        level = [root]

        while len(level)>0:
            nextLevel = []
            vals = []
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                    vals.append(node.left.val)
                else:
                    vals.append(None)
                if node.right:
                    nextLevel.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(None)
            if vals != vals[::-1]:
                return False
            level = nextLevel
        return True
