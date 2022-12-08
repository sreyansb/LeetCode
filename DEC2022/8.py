#attempt1: Had to think through quite deeply
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorderLeaves(root, leaves):
            if root:
                isLeaf = True
                if root.left:
                    isLeaf = False
                    inorderLeaves(root.left,leaves)
                if root.right:
                    isLeaf = False
                    inorderLeaves(root.right,leaves)
                if isLeaf:
                    leaves.append(root.val)
        
        leaves1 = []
        leaves2 = []
        inorderLeaves(root1, leaves1)
        inorderLeaves(root2, leaves2)
        return leaves1 == leaves2
