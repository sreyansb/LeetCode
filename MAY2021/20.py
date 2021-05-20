#attempt1: In curlevel you expect that all nodes are non-None.
#So important to check initially if the node is None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curlevel=[root]
        ans=[]
        while(curlevel):
            ans.append([])
            nextlevel=[]
            for i in curlevel:
                ans[-1].append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            curlevel=nextlevel.copy()
        return ans
                  