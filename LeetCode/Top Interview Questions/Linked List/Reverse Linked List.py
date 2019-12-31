#Reverse Linked List
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/560/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def reverseList_r(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: #base case
            return head
        
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest
