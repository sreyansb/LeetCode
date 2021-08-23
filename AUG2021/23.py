

#attempt1: GEt inorder and then perform dictionary match
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ordered=[]
        def inorder(root):
            if root:
                inorder(root.left)
                ordered.append(root.val)
                inorder(root.right)
        inorder(root)
        di={}
        for i in ordered:
            if k-i in di:
                return True
            di[i]=1
        return False
'''