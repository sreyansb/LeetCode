#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root)
                inorder(root.right)
        inorder(root)
        for i in range(len(l)-1):
            l[i].right=l[i+1]
            l[i].left=None
        l[-1].left=None
        return l[0]
            
            
                
