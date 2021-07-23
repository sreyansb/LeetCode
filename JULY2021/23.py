#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        #if it contains 1 it is sent as True
        def recurse(root):
            if not(root):
                return False
            l=recurse(root.left)
            r=recurse(root.right)
            if not(l):
                root.left=None
            if not(r):
                root.right=None
            if root.val:
                return True
            else:
                return l or r
        k=recurse(root)
        return root if k else None