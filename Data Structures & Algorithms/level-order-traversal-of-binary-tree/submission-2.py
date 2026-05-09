# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        nextLevel = [root]
        result = []
        while len(nextLevel) > 0:
            currLevel = nextLevel
            nextLevel = []
            row = []
            for node in currLevel:
                row.append(node.val)
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)


            result.append(row)
        return result



        