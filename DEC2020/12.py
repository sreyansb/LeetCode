#attempt1:60% MOST important problem of the month finding lca and deepest nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #plan-> find the deepest nodes and calculate cumulative lca for a pair
        def lca(root,n1,n2):
            if not(root):
                return None
            if root.val==n1.val or root.val==n2.val:
                return root
            leftie=lca(root.left,n1,n2)
            rightie=lca(root.right,n1,n2)
            if leftie and rightie:
                return root
            elif leftie:
                return leftie
            else:
                return rightie
        headc=root
        head=root
        curlevel=[headc]
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
        else:
            lcadone=lca(head,curlevel[0],curlevel[1])
            for i in curlevel[2:]:
                lcadone=lca(head,lcadone,i)
            return lcadone
        #curlevel has the deepest nodes
        #now we need to find pairwise LCAs
            
        
