# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trimkaro(root):
            if not(root):
                return None
            if root.val>high:
                return trimkaro(root.left)
            elif root.val<low:
                return trimkaro(root.right)
            elif root.val==low:
                root.left=None
            elif root.val==high:
                root.right=None
            root.left=trimkaro(root.left)
            root.right=trimkaro(root.right)
            return root
        return trimkaro(root)
