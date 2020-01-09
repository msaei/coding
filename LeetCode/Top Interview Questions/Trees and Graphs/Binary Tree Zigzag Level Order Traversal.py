#Binary Tree Zigzag Level Order Traversal
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        level = [root]
        res = []
        left = False
        while len(level)>0:
            next_level = []
            cur_res = []
            for node in level:
                cur_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level 
            left = not left

            res.append(cur_res if left else cur_res[::-1])
        return res
