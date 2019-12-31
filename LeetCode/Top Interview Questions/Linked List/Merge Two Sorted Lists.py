#Merge Two Sorted Lists
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/771/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode(0)
        cur = merged
        while l1 != None or l2 != None :
            if l2 == None: 
                cur.next = l1
                return merged.next
            if l1 == None:
                cur.next = l2
                return merged.next
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            cur.next = None
        return merged.next
