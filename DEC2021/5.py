#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def find(root):
            if root:
                l1,r1,l2,r2 = [None]*4
                if root.left:
                    l1 = root.left.left
                    r1 = root.left.right
                if root.right:
                    l2 = root.right.left
                    r2 = root.right.right 
                return max(root.val+find(l1)+find(l2)+find(r1)+find(r2),find(root.left)+find(root.right))
            return 0
        return find(root)
