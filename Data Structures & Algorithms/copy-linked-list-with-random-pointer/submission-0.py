"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = None
        prev = None
        copy = None
        eq = {}
        start = head
        while head != None:
            curr = Node(head.val, None, None)
            eq[curr] = head
            eq[head] = curr
            if prev != None:
                prev.next = curr
            else:
                copy = curr
            head = head.next
            prev = curr
        curr = copy
        while curr != None:
            if curr in eq and eq[curr].random in eq:
                curr.random = eq[eq[curr].random]
            curr = curr.next
        return copy
            
        