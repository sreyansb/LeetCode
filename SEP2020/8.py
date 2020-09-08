# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        li=[]
        def find(root,sumi):
            if root:
                if not(root.left) and not(root.right):
                    li.append((sumi<<1) + root.val)
                find(root.left,(sumi<<1)+root.val)
                find(root.right,(sumi<<1)+root.val)
        find(root,0)
        return sum(li)
        
