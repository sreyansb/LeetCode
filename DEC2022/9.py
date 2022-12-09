#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = [-float('inf')]
        def findMaxDiff(root,currentMax, currentMin):
            if root:
                maxDiff[0] = max(maxDiff[0], abs(root.val-currentMax)) if currentMax != -float('inf') else maxDiff[0]
                maxDiff[0] = max(maxDiff[0], abs(root.val-currentMin)) if currentMin != float('inf') else maxDiff[0]
                findMaxDiff(root.left, max(currentMax,root.val), min(currentMin, root.val))
                findMaxDiff(root.right, max(currentMax,root.val), min(currentMin, root.val))
        findMaxDiff(root,-float('inf'), float('inf'))
        return maxDiff[0]

        

#attempt1: Slow. You don't need all ancestors. I sort of figured out
#in BST but don't why I couldn't get the optimized result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = [-float('inf')]
        def findMaxDiff(root,ancestors=set()):
            if root:
                maxDiff[0] = max([maxDiff[0]] + [abs(root.val-ancestor) for ancestor in ancestors])
                findMaxDiff(root.left, ancestors|{root.val})
                findMaxDiff(root.right, ancestors|{root.val})
        findMaxDiff(root,set())
        return maxDiff[0]

        
