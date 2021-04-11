# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        lev=[root]
        ans=[0]
        while(lev):
            nextl=[]
            ans[0]=0
            for i in lev:
                ans[0]+=i.val
                if i.left:
                    nextl.append(i.left)
                if i.right:
                    nextl.append(i.right)
            lev=nextl.copy()
            del nextl
        return ans[0]
