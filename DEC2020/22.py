#attempt1: needed help. get the length of left and right subtrees and check
#even the subtrees should also be right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not(root):
            return True
        def height(root):
            if root:
                return max(height(root.left),height(root.right))+1
            return 0
        def checklen(root):
            if not(root):
                return True
            l=height(root.left)
            r=height(root.right)
            return (abs(l-r)<=1 and checklen(root.left) and checklen(root.right))
        return checklen(root)
        
