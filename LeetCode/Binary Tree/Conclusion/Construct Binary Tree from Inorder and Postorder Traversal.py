#Construct Binary Tree from Inorder and Postorder Traversal
#https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root_val = postorder.pop()
        root_ind = inorder.index(root_val)
        left_inorder = inorder[:root_ind]
        right_inorder = inorder[root_ind + 1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):]
        root = TreeNode(root_val)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
        
