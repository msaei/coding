#Odd Even Linked List
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
    def oddEvenList_2(self, head: ListNode) -> ListNode:
        even_head = head.next if head else None
        cur = head
        while cur:
            temp = cur.next
            cur.next = cur.next.next if cur.next else None
            if temp:
                temp.next = temp.next.next if temp.next else None
            if cur.next == None:
                cur.next = even_head
                break
            cur = cur.next
        return head
        
            
    def oddEvenList_1(self, head: ListNode) -> ListNode:

        holder = ListNode(-1)
        res = holder
        cur = head
        while cur:
            res.next = ListNode(cur.val)
            res = res.next
            cur = cur.next.next if cur.next else None
        cur = head.next if head else None
        while cur:
            res.next = ListNode(cur.val)
            res = res.next
            cur = cur.next.next if cur.next else None
        
        return holder.next
