#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def finder(root,val):
            if root:
                newval = (val<<1) + root.val
                if not(root.left) and not(root.right):
                    ans[0] += newval
                    return
                finder(root.left,newval)
                finder(root.right,newval)
        finder(root,0)
        return ans[0]
                    
        
