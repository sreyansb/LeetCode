#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        finlist = []
        def inorder(root):
            if root:
                inorder(root.left)
                finlist.append(root)
                inorder(root.right)
        inorder(root)
        n = len(finlist)
        sorted_finlist = sorted([x.val for x in finlist])
        #print(finlist,sorted_finlist)
        for i in range(n):
            finlist[i].val = sorted_finlist[i]
        
        
                
