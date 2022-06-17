#Attempt2: TOOK HELP
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        visited = {None}
        def dfs(root,parent = None):
            if root:
                dfs(root.left,root)
                dfs(root.right,root)
                
                if (root not in visited and parent == None) or (root.left not in visited) or (root.right not in visited):
                    ans[0] += 1
                    visited.add(root)
                    visited.add(parent)
                    visited.add(root.left)
                    visited.add(root.right)
        
        dfs(root)
        return ans[0]

#attempt1: WA bcoz a node might not have children but its sibling covers
#the parent, so no need
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            levels = []
            currentlevel = [root]
            while(currentlevel):
                levels.append(currentlevel.copy())
                nextlevel = []
                for node in currentlevel:
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                currentlevel = nextlevel.copy()
            return levels
        
        levels = bfs(root)
        if len(levels) <= 2:
            return 1
        ans = 0
        for level in levels[-2::-2]:
            ans += len(level)
        return ans
        
'''
