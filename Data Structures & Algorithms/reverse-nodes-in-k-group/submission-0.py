# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''

1   2|  3   4|  5
2   1|  3   4|  5
2   1|  4   3|  5

k=2

'''
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groups = self.length(head) // k
        newHead = None
        prevTail = None

        for g in range(groups):
            tail = head
            for i in range(k):
                tail = tail.next
            revHead, revTail = self.reverse(head, tail)
            if not newHead:
                newHead = revHead
            if prevTail:
                prevTail.next = revHead
            prevTail = revTail
            head = tail
        
        if prevTail:
            prevTail.next = head
        
        return newHead or head


    
    def reverse(self, head, tail):
        prev, curr = None, head
        while curr != tail:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev, head
        
    def length(self, head):
        curr = head
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res