#LSerialize and Deserialize Binary Tree
#https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        level = [root]
        res = str(root.val) + ' '
        while len(level)>0:
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    res += str(node.left.val) + ' '
                else:
                    res += 'n '
                if node.right:
                    next_level.append(node.right)
                    res += str(node.right.val) + ' '
                else:
                    res += 'n '
            level = next_level[:]
        print(res)
        return res
                
                
        
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        vals = data.split()
        nodes =[]
        for val in vals:
            if val == 'n':
                nodes.append(None)
            else:
                nodes.append(TreeNode(int(val)))
        pi = 0
        ci = 0
        while ci < len(nodes):
            parent = nodes[pi]
            ci += 1
            parent.left = nodes[ci]
            ci += 1
            parent.right = nodes[ci]
            pi += 1
            while nodes[pi] == None:
                pi += 1
                if pi >= len(nodes):
                    return nodes[0]
                
        return nodes[0]
            
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
