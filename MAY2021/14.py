#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        ans=[]
        def preorder(root):
            if root:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        n=len(ans)
        index=0
        rootc=root
        while(index<n):
            root.val=ans[index]
            root.left=None
            if index!=n-1:
                root.right=TreeNode()

                root=root.right
            index+=1
        
        return rootc
            
        
