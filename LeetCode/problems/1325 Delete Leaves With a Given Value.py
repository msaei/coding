#1325. Delete Leaves With a Given Value
#https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root, target):
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.val != target or root.left or root.right:
                return root
        
    def removeLeafNodes_m(self, root: TreeNode, target: int) -> TreeNode:
        #postorder travers
        def postorder(r: TreeNode, p: TreeNode, isLeft = True):
            if r == None:
                return
            postorder(r.left, r, True)
            postorder(r.right, r, False)
            
            if r.left == None and r.right == None and r.val == target:
                if isLeft:
                    p.left = None
                else:
                    p.right = None
        dummy = TreeNode(0)
        dummy.left = root
        postorder(root, dummy, True)
        return dummy.left
