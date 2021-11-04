#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        curlevel = [root]
        ans = 0
        while(curlevel):
            nextlevel = []
            for i in curlevel:
                if i.left:
                    nextlevel.append(i.left)
                    if not(i.left.left) and not(i.left.right):
                        ans += i.left.val
                if i.right:
                    nextlevel.append(i.right)
            curlevel = nextlevel
        return ans
