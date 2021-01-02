#attempt1: quite an easy problem
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def finder(cloned):
            if cloned:
                if cloned.val==target.val:
                    return cloned
                return finder(cloned.left) or finder(cloned.right)
        return finder(cloned)
            
        
