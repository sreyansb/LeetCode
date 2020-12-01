#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def recurse(root):
            if not(root):
                return 0
            return 1+max(recurse(root.left),recurse(root.right))
        return recurse(root)
        
