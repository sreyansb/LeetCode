#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            if root:
                root.left = prune(root.left)
                root.right = prune(root.right)
                return root if (root.left or root.right or root.val == 1) else None
            return None
        return prune(root)
        
