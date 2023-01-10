#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(root1,root2):
            if root1:
                if not(root2):
                    return False
                return root1.val == root2.val and isSame(root1.left,root2.left) and isSame(root1.right, root2.right)
            return not(root2)
        return isSame(p,q)
