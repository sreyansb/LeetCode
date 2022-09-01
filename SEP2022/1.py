#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        def findpath(node,maxvalue):
            if node:
                if node.val >= maxvalue:
                    ans[0] += 1
                findpath(node.left,max(maxvalue,node.val))
                findpath(node.right,max(maxvalue,node.val))
        findpath(root,-float('inf'))
        return ans[0]
                
