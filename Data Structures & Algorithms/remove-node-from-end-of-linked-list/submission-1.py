# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None 
        prev = None 
        while head:
            nxt = head.next
            head.next = prev 
            prev = head 
            head = nxt 
        head = prev 
        curr = ListNode(0, head)
        dummy = curr
        for _ in range(n-1):
            dummy = dummy.next 
        dummy.next = dummy.next.next
        prev = None
        head = curr.next 
        while head:
            nxt = head.next
            head.next = prev 
            prev = head 
            head = nxt 
        return prev

            