#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findlca(root,p,q):
            if not(root):
                return None
            if root.val==p:
                return root
            if root.val==q:
                return root
            l=findlca(root.left,p,q)
            r=findlca(root.right,p,q)
            if l and r:
                return root
            return l or r
        return findlca(root,p.val,q.val)
        