#attempt2: 80% and 30%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        dp={}
        def calcre(root):
            #returns a tuple(x,y) where x->represents taking the root and y->represents ot taking the root
            if not(root):
                return (0,0)
            v1=calcre(root.left)
            v2=calcre(root.right)
            return (root.val+v1[1]+v2[1],max(v1)+max(v2))
        return (max(calcre(root)))
        

#attempt1: 30% and 30%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        dp={}
        def calcre(root):
            if not(root):
                return 0
            if root in dp:
                return dp[root]
            val=0
            rl=calcre(root.left)
            rr=calcre(root.right)
            rll,rlr,rrl,rrr=0,0,0,0
            if root.left:
                rll=calcre(root.left.left)
                rlr=calcre(root.left.right)
            if root.right:
                rrl=calcre(root.right.left)
                rrr=calcre(root.right.right)
            val=max(rl+rr,root.val+rll+rlr+rrl+rrr)
            dp[root]=val
            return val
        return (calcre(root))
'''       
