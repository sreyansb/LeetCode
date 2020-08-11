# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,sum,ans,visited):
    if root:
        if root.left==None and root.right==None and root.val==sum:
            visited.append(root.val)
            ans.append(visited)
        helper(root.left,sum-root.val,ans,visited+[root.val])
        helper(root.right,sum-root.val,ans,visited+[root.val])
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans=[]
        helper(root,sum,ans,[])
        return ans
        
