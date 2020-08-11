# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root):
    if not(root):
        return False
    if root.val:
        root.left=root.left if helper(root.left) else None
        root.right=root.right if helper(root.right) else None
        return True
    else:
        root.left=root.left if helper(root.left) else None
        root.right=root.right if helper(root.right) else None
        if root.left or root.right:
            return True
        else:
            return False
        
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if helper(root):
            return root
        else:
            return None
        
            
                
        
