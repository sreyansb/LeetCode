# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,ans):
    if root:
        if root.left:
            if not(root.left.left) and not(root.left.right):
                ans[0]+=root.left.val
            else:
                helper(root.left,ans)
        helper(root.right,ans)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans=[0]
        helper(root,ans)
        return ans[0]
        
