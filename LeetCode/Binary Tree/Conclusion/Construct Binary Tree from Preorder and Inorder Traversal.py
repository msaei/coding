#Construct Binary Tree from Preorder and Inorder Traversal
#https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root_ind = inorder.index(root_val)
        left_inorder = inorder[:root_ind]
        right_inorder = inorder[root_ind + 1:]
        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]
        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
        
