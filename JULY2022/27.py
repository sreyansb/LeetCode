#attempt6:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        ans = []
        def preorder(root):
            if root:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        rootc = root
        for val in ans[:-1]:
            rootc.val = val
            rootc.left = None
            rootc.right = TreeNode()
            rootc = rootc.right
        rootc.val = ans[-1]
        return
                
