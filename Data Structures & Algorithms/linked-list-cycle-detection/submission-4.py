# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None):
            return False
        slowPointer = head.next
        if(slowPointer == None or slowPointer.next == None):
            return False
        fastPointer = head.next.next

        while slowPointer != None and fastPointer != None:
            if(slowPointer == fastPointer):
                return True
            slowPointer = slowPointer.next
            if(fastPointer.next == None):
                return False
            fastPointer = fastPointer.next.next

        return False