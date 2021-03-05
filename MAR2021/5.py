#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        curlevel=[root]
        ans=[]
        while(curlevel):
            nextlevel=[]
            summy=0
            count=0
            for i in curlevel:
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
                summy+=i.val
                count+=1
            ans.append(summy/count)
            curlevel=nextlevel.copy()
            del nextlevel
        return ans
