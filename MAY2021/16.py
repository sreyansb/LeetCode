#attempt2:TOOK HELP
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans=[0]
        visited={None}
        def dfs(node,parent=None):
            if node:
                dfs(node.left,node)
                dfs(node.right,node)
                
                if (parent is None and node not in visited) or (node.left not in visited) or (node.right not in visited):
                    ans[0]+=1
                    visited.add(parent)
                    visited.add(node)
                    visited.add(node.left)
                    visited.add(node.right)
        dfs(root)
        return ans[0]

#attempt1:TOOK HINT WA because of [0,null,0,0,0,null,null,null,0]
#My Code would give a problem because answer would be 3 instead of 2
'''
     0
      \
       0
      / \
     0   0
          \
           0
'''
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans=[0]
        if not(root):
            return 0
        layers=[]
        curlayer=[root]
        while(curlayer):
            layers.append(curlayer.copy())
            newlayer=[]
            for i in curlayer:
                if i.left:
                    newlayer.append(i.left)
                if i.right:
                    newlayer.append(i.right)
            curlayer=newlayer.copy()
            del newlayer
        totans=0
        while(layers):
            if len(layers)<3:
                totans+=len(layers[0])
                break
            else:
                totans+=len(layers[-2])
                layers=layers[:-3]
        return totans
'''
