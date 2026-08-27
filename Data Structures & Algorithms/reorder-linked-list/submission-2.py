# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return 
        fast = head 
        slow = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        middle = slow 
        newHead = middle.next
        middle.next = None
        prev = None
        while newHead:
            nxt = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = nxt
        newHead = prev
        newList = head
        p1 = head 
        p2 = newHead
        while p2:
            nxt1 = p1.next
            nxt2 = p2.next 

            p1.next = p2
            p2.next = nxt1

            p1 = nxt1
            p2 = nxt2