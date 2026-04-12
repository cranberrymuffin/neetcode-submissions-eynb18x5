# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        empty = 0
        curr = None
        while empty != len(lists):
            empty = 0
            minNode = None
            for idx, ll in enumerate(lists):
                if ll != None:
                    if minNode == None or ll.val < lists[minNode].val:
                        minNode = idx 
                else:
                    empty += 1
            if minNode == None:
                break
            nextNode = lists[minNode]
            lists[minNode] = lists[minNode].next
            if result == None:
                result = nextNode
                curr = result
            else:
                curr.next = nextNode
                curr = curr.next
        
        return result
        