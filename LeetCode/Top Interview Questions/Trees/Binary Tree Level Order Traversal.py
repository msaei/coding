#Binary Tree Level Order Traversal
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/628/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        level = [root]
        result = []
        while len(level)>0:
            nextLevel = []
            levelResult = []
            for node in level:
                levelResult.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            result.append(levelResult)
            level = nextLevel[:]
        return result
