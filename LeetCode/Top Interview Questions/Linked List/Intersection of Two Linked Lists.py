#Intersection of Two Linked Lists
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

class Solution:

    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
    
    
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointerA = headA
        pointerB = headB
        swap = 0
        while pointerA or pointerB:
            if pointerA == pointerB:
                return pointerA
            pointerA = pointerA.next if pointerA else None
            pointerB = pointerB.next if pointerB else None
            
            if pointerA == None and swap <2:
                pointerA = headB
                swap += 1
            if pointerB == None and swap <2:
                pointerB = headA
                swap +=1
        
