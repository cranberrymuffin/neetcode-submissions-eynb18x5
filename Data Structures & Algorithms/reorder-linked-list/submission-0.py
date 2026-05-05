# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return None

        prev = None
        curr = head
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

    def printList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr != None:
            curr = curr.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return None
        size = 0
        curr = head
        while curr != None:
            size += 1
            curr = curr.next

        secondHalf = None
        curr = head
        halfSize = math.ceil(size/2)
        prev = None
        while halfSize > 0:
            prev = curr
            curr = curr.next
            halfSize -= 1
        
        prev.next = None

        secondHalf = self.reverseList(curr)

        curr = head
        secondHalfCurr = secondHalf
        while curr != None and secondHalfCurr != None:
            nex = curr.next
            secondHalfCurrNext = secondHalfCurr.next
            curr.next = secondHalfCurr
            secondHalfCurr.next = nex

            curr = nex
            secondHalfCurr = secondHalfCurrNext

        