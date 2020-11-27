#attempt1: 60% and 40%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        curlevel=[root]
        parent=None
        while(curlevel):
            nextlevel=[]
            parent=curlevel.copy()
            for i in curlevel:
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            curlevel=nextlevel.copy()
        return parent[0].val
        
