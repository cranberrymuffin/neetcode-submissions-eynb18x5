# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 == None and tree2 == None:
            return True
        elif tree1 == None or tree2 == None:
            return False
        elif tree1.val != tree2.val:
            return False
        return self.isSameTree(tree1.right, tree2.right) and self.isSameTree(tree1.left, tree2.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot != None:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        elif self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        