# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp != None:
            length += 1
            tmp = tmp.next
        
        if(length - n == 0):
            return head.next

        tmp = head
        prev = None
        for i in range(length - n):
            prev = tmp
            tmp = tmp.next
        
        prev.next = tmp.next
        return head

            
            

        