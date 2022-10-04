#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findAns(node,sumLeft):
            if node:
                if not(node.left) and not(node.right):
                    return sumLeft == node.val
                return findAns(node.left,sumLeft-node.val) or findAns(node.right,sumLeft-node.val)
            return False
        return findAns(root,targetSum)
        
