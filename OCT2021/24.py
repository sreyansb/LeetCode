#attempt2:


#attempt1: O(n) solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        nodes = [0]
        def findheight(root):
            if root:
                nodes[0] += 1
                return 1+max(findheight(root.left),findheight(root.right))
            return 0
        findheight(root)
        return nodes[0]
'''
