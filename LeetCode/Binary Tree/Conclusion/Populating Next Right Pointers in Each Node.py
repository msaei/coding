#Populating Next Right Pointers in Each Node
#https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        cur_level = [root]
        while len(cur_level) > 0:
            next_level = []
            for i in range(len(cur_level)):
                cur_node = cur_level[i]
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
                if i < (len(cur_level) -1):
                    cur_node.next = cur_level[i+1]
            cur_level = next_level[:]
        return root
        
