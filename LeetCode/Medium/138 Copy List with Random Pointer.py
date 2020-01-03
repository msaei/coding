#138 Copy List with Random Pointer
#https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        node_map = {}
        source = head
        while source:
            cp = Node(source.val)
            node_map[source] = cp
            source = source.next
            
        source = head
        while source:
            cp = node_map[source]
            if source.next:
                cp.next = node_map[source.next]
            if source.random:
                cp.random = node_map[source.random]
            source = source.next
        return node_map[head]
            
