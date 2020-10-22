# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getpath(arr,root,value):
            arr.append(root)
            if root.val==value:
                return True
            if (root.left and getpath(arr,root.left,value)) or (root.right and getpath(arr,root.right,value)):
                return True
            else:
                arr.pop()
        parr=[]
        qarr=[]
        getpath(parr,root,p.val)
        getpath(qarr,root,q.val)
        i=0
        j=0
        while(i<len(parr) and j<len(qarr)):
            if parr[i].val!=qarr[j].val:
                break
            i+=1
            j+=1
        return parr[i-1]
                
        
