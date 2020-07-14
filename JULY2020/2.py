# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#easy logic, couldn't get it
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        curlev=[root]
        result=[]
        curans=[]
        while(curlev):
            curans=[]
            nextlev=[]
            for i in curlev:
                curans.append(i.val)
                if i.left!=None:
                    nextlev.append(i.left)
                if i.right!=None:
                    nextlev.append(i.right)
            curlev=nextlev
            result.append(curans)
        result.reverse()
        return result
            
            
        
        
        
