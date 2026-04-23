# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTH(root, float('-inf'),float('inf'))

    def isValidBSTH(self, root: Optional[TreeNode], currMin, currMax) -> bool:
        if root == None:
            return True

        if root.val >= currMax or root.val <= currMin:
            print(currMin)
            print(currMax)
            print(root.val)
            return False
        elif root.right != None and root.val >= root.right.val:
            return False
        elif root.left != None and root.val <= root.left.val:
            return False
        else:
            return self.isValidBSTH(root.right, root.val,  currMax) and self.isValidBSTH(root.left, currMin,  root.val)