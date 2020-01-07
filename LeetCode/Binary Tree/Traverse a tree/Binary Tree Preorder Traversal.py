#Binary Tree Preorder Traversal
#https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

class Solution:
    def preorderTraversal_r(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        return [root.val] + self.preorderTraversal_r(root.left) + self.preorderTraversal_r(root.right)
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        nodes = [root]
        result = []
        while len(nodes) > 0:
            current = nodes.pop()
            result.append(current.val)
            if current.right:
                nodes.append(current.right)
            if current.left:
                nodes.append(current.left)
        return result
