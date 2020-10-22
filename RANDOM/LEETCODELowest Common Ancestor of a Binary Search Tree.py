#ATTEMPT1: 86.55% and 99.98%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minval=min(p.val,q.val)
        maxval=max(p.val,q.val)
        def getroot(root):
            while(root):
                if root.val>maxval:
                    root=root.left
                elif root.val<minval:
                    root=root.right
                else:
                    return root
            return root
        return getroot(root)
        
