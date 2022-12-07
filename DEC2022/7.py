#attemp1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def findAns(root):
            if root:
                if (low <= root.val <= high):
                    ans[0] += root.val
                findAns(root.left)
                findAns(root.right)
        findAns(root)
        return ans[0]
        
