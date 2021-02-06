#attempt1:91%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not(root):
            return []
        curlevel=[root]
        ans=[]
        while(curlevel):
            nextlevel=[]
            for i in curlevel:
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            ans.append(curlevel[-1].val)
            curlevel=nextlevel
        return ans
