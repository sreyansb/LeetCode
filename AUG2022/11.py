#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateBST(root,minVal = -float('inf'),maxVal = float('inf')):
            if root and minVal<root.val<maxVal:
                return validateBST(root.left,minVal,root.val) and validateBST(root.right,root.val,maxVal)
            return True if not(root) else False
        return validateBST(root)
        
