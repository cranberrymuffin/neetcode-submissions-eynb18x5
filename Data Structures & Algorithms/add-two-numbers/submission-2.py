# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        curr1 = l1
        curr2 = l2
        prev = None
        while (curr1 != None and curr2 != None):
            curr1.val = curr1.val + curr2.val + remainder
            if curr1.val >= 10:
                curr1.val = curr1.val - 10
                remainder = 1
            else:
                remainder = 0
            prev = curr1
            curr1 = curr1.next
            curr2 = curr2.next

        if curr2 != None:
            prev.next = curr2
            curr1 = prev.next
        
        while curr1 != None:
            curr1.val = curr1.val + remainder
            if curr1.val >= 10:
                curr1.val = curr1.val - 10
                remainder = 1
            else:
                remainder = 0
            prev = curr1
            curr1 = curr1.next
        print(remainder)
        if remainder > 0:
            prev.next = ListNode(val=remainder)


        return l1