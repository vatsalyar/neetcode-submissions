# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
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
        ret = head
        i = 1
        while head and newHead:
            if i%2 == 1:
                new_nxt = head.next
                newList.next = newHead
                head = new_nxt
            else:
                new_nxt = newHead.next
                newList.next = head
                newHead = new_nxt
            i+=1
            newList = newList.next
        head = ret