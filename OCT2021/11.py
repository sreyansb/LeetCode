#attempt1: The idea is that diameter of a tree at a "node"
#is the sum of the heights of the left and right subtrees
#And at every node we need to find the sum of heights and eventually get the max
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=[-float('inf')]
        def recurse(root):
            if root:
                maxr=recurse(root.right)
                maxl=recurse(root.left)
                ans[0]=max(ans[0],maxl+maxr)
                return 1+max(maxl,maxr)
            else:
                return 0
        recurse(root)
        return ans[0]