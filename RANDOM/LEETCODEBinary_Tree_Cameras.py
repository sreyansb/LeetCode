

#attempt1: WA-tried finding height of tree and divided it by 2
#wrong idea because nodes cant monitor their siblings
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def findheight(root):
            if root:
                return 1+max(findheight(root.left),findheight(root.right))
            return 0
        return max(1,findheight(root)//2)
"""
