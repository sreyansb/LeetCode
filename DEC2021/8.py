#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def recurse(root):
            if root:
                l = recurse(root.left)
                r = recurse(root.right)
                ans[0] += abs(l-r)
                return l+r+root.val                
            return 0
        recurse(root)
        return ans[0]
        
