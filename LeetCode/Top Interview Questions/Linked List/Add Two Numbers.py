#Add Two Numbers
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # go through l1 and l2 and add them to accumulator
        acc = 0
        power = 1
        while l1:
            acc += l1.val * power
            l1 = l1.next
            power *= 10
        power = 1
        while l2:
            acc += l2.val * power
            l2 = l2.next
            power *=10
            
        # create listnode out of accumulator
        if acc == 0:
            return ListNode(0)
        holder = ListNode(-1)
        prev = holder
        while acc > 0:
            cur = ListNode(acc % 10)
            prev.next = cur
            acc //= 10
            prev = cur
        return holder.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = node =  ListNode(-1)
        carry = 0
        
        while l1 or l2:
            x = carry
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next
                
            digit, carry = x%10, x//10
            
            node.next = ListNode(digit)
            node = node.next
            
        if carry != 0:
            node.next = ListNode(carry)
            node = node.next
            
        return res.next
