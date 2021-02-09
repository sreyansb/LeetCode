#attempt1:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def pre(root,rightval=[0]):
            if root:
                pre(root.right,rightval)
                rightval[0]+=root.val
                root.val=rightval[0]
                pre(root.left,rightval)
        pre(root)
        return root
        
