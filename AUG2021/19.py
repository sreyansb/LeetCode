#aattempt 2 and 1: TOOK HINT.
#Very important to remember that this problem is a function of the total sum
#  And the sum of two parts depens on the SUM of the two subtrees which can hence
#be calculated using just one of the node's sum and other is totalsum-current


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def calcsum(node):
            if not node:
                return 0
            node.val+=calcsum(node.left)+calcsum(node.right)
            return node.val
        calcsum(root)
        totsum=root.val
        maxie=[-float('inf')]
        def findmin(node):
            if not node:
                return
            maxie[0]=max(maxie[0],node.val*(totsum-node.val))
            findmin(node.left)
            findmin(node.right)
        findmin(root)
        return maxie[0]%(1000000007)
            
        