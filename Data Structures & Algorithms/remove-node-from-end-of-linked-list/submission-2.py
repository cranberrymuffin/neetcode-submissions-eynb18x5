# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next

        toRemove = length - n
        curr = head
        prev = None
        i = 0
        while i != toRemove:
            prev = curr
            curr = curr.next
            i += 1
        
        if prev == None:
            return head.next
        else:
            prev.next = curr.next
            curr.next = None
        
        return head