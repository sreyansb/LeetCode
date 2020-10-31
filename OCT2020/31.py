#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        realorder=[]
        def getinorder(root):
            if root:
                getinorder(root.left)
                realorder.append(root.val)
                getinorder(root.right)
        getinorder(root)
        actual=sorted(realorder)
        v1,v2=0,0
        for i in range(len(realorder)):
            if actual[i]!=realorder[i]:
                v1=actual[i]
                v2=realorder[i]
                break
        def changevalue(root,v1,v2):
            if root:
                if root.val==v1:
                    root.val=v2
                elif root.val==v2:
                    root.val=v1
                changevalue(root.left,v1,v2)
                changevalue(root.right,v1,v2)
        changevalue(root,v1,v2)
"""
