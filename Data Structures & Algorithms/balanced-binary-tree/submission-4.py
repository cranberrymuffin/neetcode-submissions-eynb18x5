# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.findHeight(root)
        return self.balanced

    def findHeight(self, root: Optional[TreeNode]) -> int:
        if root == None or not self.balanced:
            return 0
        leftHeight = 1 + self.findHeight(root.right)
        rightHeight = 1 + self.findHeight(root.left)
        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
            return 0
        return max(leftHeight, rightHeight)


