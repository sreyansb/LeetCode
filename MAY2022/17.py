#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def recurse(original,cloned,target):
            if original == target:
                return cloned
            if not(original):
                return None
            return recurse(original.left,cloned.left,target) or recurse(original.right,cloned.right,target)
        return recurse(original,cloned,target)
        
