#Lowest Common Ancestor of a Binary Tree
#https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # create parent dictionary
        parent = {root: None}
        stack = [root]
        while len(stack)>0:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
                parent[cur.left] = cur
            if cur.right:
                stack.append(cur.right)
                parent[cur.right] = cur
        # create path to p
        pathToP = []
        cur = p
        while cur:
            pathToP.append(cur)
            cur = parent[cur]
        print(*map(lambda x:x.val, pathToP))
        # create path to q
        pathToQ = []
        cur = q
        while cur:
            pathToQ.append(cur)
            cur = parent[cur]
        print(*map(lambda x:x.val, pathToQ))
        # search for last mutual parent
        i = -1
        
        while -i <= len(pathToP) and -i <= len(pathToQ) and pathToP[i] == pathToQ[i]:
            i -= 1
        return pathToP[i + 1]
        
