# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def helper(root,sum,ans,visited):
    if root:
        visited.append(root.val)        
        helper(root.left,sum,ans,visited)
        helper(root.right,sum,ans,visited)
        temp=0
        for i in visited[::-1]:#we do reverse of visited because higher values ka problem
            temp+=i
            if temp==sum:
                ans[0]+=1
        visited.pop()
            
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ans=[0]
        helper(root,sum,ans,[])
        return ans[0]

obj=Solution()
root=TreeNode()
root.val=-2
root.right=TreeNode()
root.right.val=-3
sum=-5
print(obj.pathSum(root,sum))

        
