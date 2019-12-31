#Linked List Cycle
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/773/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = {}
        while head:
            if head in nodes.keys():
                return True
            nodes[head] =  1
            head = head.next
        return False
