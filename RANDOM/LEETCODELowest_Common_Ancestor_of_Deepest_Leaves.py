#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def lca(root,n1,n2):
            if not(root):
                return None
            if root.val==n1.val or root.val==n2.val:
                return root
            leftie=lca(root.left,n1,n2)
            rightie=lca(root.right,n1,n2)
            if leftie and rightie:
                return root
            if leftie:
                return leftie
            else:
                return rightie
        #get deepest
        curlevel=[root]
        while(curlevel):
            nextlevel=[]
            for i in curlevel:
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if not(nextlevel):
                break
            curlevel=nextlevel.copy()
        if len(curlevel)==1:
            return curlevel[0]
        lcadone=lca(root,curlevel[0],curlevel[1])
        for i in curlevel[2:]:
            lcadone=lca(root,lcadone,i)
        return lcadone
                
        
