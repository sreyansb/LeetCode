#attempt1: 32ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def recurse(root,csum):
            if root:
                temp = csum*10 + root.val
                if not(root.left) and not(root.right):
                    ans[0] += temp
                recurse(root.left,temp)
                recurse(root.right,temp)
        recurse(root,0)
        return ans[0]
                
            
        
