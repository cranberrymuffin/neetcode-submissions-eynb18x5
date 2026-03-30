# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = None
        curr = None

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                if curr == None:
                    sortedList = list1
                    curr = sortedList
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if curr == None:
                    sortedList = list2
                    curr = sortedList
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next

        if list1 != None:
            if curr != None:
                curr.next = list1
            else:
                return list1
        elif list2 != None:
            if curr != None:
                curr.next = list2
            else:
                return list2
    
        return sortedList 