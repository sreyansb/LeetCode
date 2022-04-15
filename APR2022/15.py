#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trimroot(root):
            if root:
                if root.val<low:
                    return trimroot(root.right)
                elif root.val>high:
                    return trimroot(root.left)
                else:
                    root.left = trimroot(root.left)
                    root.right = trimroot(root.right)
            return root
        return trimroot(root)
