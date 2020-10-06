# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#ATTEMPT1 : 94% and 10% 
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not(root):
            return TreeNode(val=val)#very important condition
            #cant return None
        rootcopy=root
        parent=None
        while(rootcopy):
            parent=rootcopy
            if val<rootcopy.val:
                rootcopy=rootcopy.left
            else:
                rootcopy=rootcopy.right
        if val<parent.val:
            parent.left=TreeNode(val=val)
        else:
            parent.right=TreeNode(val=val)
        return root
        
