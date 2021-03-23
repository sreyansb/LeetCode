#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans=[0]
        
        def check(s):
            vals=[i%2 for i in s]
            if 1 not in vals or (vals.count(1)==1):
                #print(s)
                ans[0]+=1
        
        def dfs(root,curli=[0,0,0,0,0,0,0,0,0,0]):
            if not(root.left) and not(root.right):
                curli[root.val]+=1
                check(curli)
                curli[root.val]-=1
            else:
                curli[root.val]+=1
                if root.left:
                    dfs(root.left,curli)
                if root.right:
                    dfs(root.right,curli)
                curli[root.val]-=1        
        dfs(root)
        return ans[0]
                
            
        
