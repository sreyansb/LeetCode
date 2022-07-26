#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root):
            if not(root):
                return None
            if root == p or root==q:
                return root
            ansleft = lca(root.left)
            ansright = lca(root.right)
            if ansleft and ansright:
                return root
            return ansleft or ansright
        
        return lca(root)
        
