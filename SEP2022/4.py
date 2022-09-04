#attempt1:
from itertools import groupby
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positionedNodes = {}
        def traverseTree(root,xpos,ypos):
            if root:
                if ypos not in positionedNodes:
                    positionedNodes[ypos] = []
                positionedNodes[ypos].append((xpos,root.val))
                if root.left:
                    traverseTree(root.left,xpos+1,ypos-1)
                if root.right:
                    traverseTree(root.right,xpos+1,ypos+1)
        traverseTree(root,0,0)
        ans = []
        for col in sorted(positionedNodes.keys()):
            ans.append([x[1] for x in sorted(positionedNodes[col],key = lambda y:(y[0],y[1]))])
        return ans
                    
        
