#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        maxdiff = [-float('inf')]
        def findmaxdiff(node,maxt,mint):
            if node:
                maxt = max(maxt,node.val)
                mint = min(mint,node.val)
                maxdiff[0] = max(maxdiff[0],maxt-mint)
                findmaxdiff(node.left,maxt,mint)
                findmaxdiff(node.right,maxt,mint)
        findmaxdiff(root,-float('inf'),float('inf'))
        return maxdiff[0]
                
        
