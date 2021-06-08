#attempt1: The node is the element at the top and subsequent elements are after it
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index=[0]
        def dfs(start,end):
            if start>end:
                return None
            a=TreeNode(preorder[index[0]])
            pos=inorder.index(preorder[index[0]])
            if start<=pos-1:
                index[0]+=1
                a.left=dfs(start,pos-1)
            if pos+1<=end:
                index[0]+=1
                a.right=dfs(pos+1,end)
            return a
        return dfs(0,len(preorder)-1)