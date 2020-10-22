#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not(root):
            return 0
        minl=[10**6]
        def depthfinder(root):
            if not(root.left) and not(root.right):
                return 0 
            else:
                if root.left and root.right:
                    return min(1+depthfinder(root.left),1+depthfinder(root.right))
                if root.right:
                    return 1+depthfinder(root.right)
                if root.left:
                    return 1+depthfinder(root.left)
        return 1+depthfinder(root)

#attempt1: AC slow
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not(root):
            return 0
        minl=[10**6]
        def depthfinder(root,curl):
            if not(root.left) and not(root.right):
                minl[0]=min(minl[0],curl)
                return
            else:
                if root.left:
                    depthfinder(root.left,curl+1)
                if root.right:
                    depthfinder(root.right,curl+1)
        depthfinder(root,1)
        return minl[0]
"""
