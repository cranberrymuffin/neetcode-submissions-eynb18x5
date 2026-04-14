# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if abs(self.height(root.right) - self.height(root.left)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(1 + self.height(root.right), 1 + self.height(root.left))