# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inpre(root,valgreat=[0]):
            if root:
                temp=root.val
                inpre(root.right,valgreat)
                root.val+=valgreat[0]
                valgreat[0]+=temp
                inpre(root.left,valgreat)
                print(temp,root.val)
        inpre(root)
        return root
                
        
