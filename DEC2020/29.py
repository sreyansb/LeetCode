#attempt1:DFS is just O(n) algo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        def dfs(root,di):
            if root:r
                if root.val not in di:
                    di[root.val]=0
                di[root.val]+=1
                if root.left==None and root.right==None:
                    #print("HERE",di)
                    odd=0
                    for i in di:
                        if di[i]%2:
                            odd+=1
                        if odd>1:
                            break
                    di[root.val]-=1
                    return 0 if odd>1 else 1
                ans1,ans2=0,0
                if root.left:
                    ans1=dfs(root.left,di)
                if root.right:
                    ans2=dfs(root.right,di)
                di[root.val]-=1
                return ans1+ans2
        return dfs(root,{})
                