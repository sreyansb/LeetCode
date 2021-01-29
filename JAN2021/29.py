#attempt2:
#Ordered Dict didn't help - need to see why

#attempt1:WA because didn't see that it has to be sorted on node values' as well.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        di={}
        def recur(root,x,y):
            if root:
                if x not in di:
                    di[x]=[]
                di[x].append((y,x,root.val))
                recur(root.left,x-1,y+1)
                recur(root.right,x+1,y+1)
        recur(root,0,0)
        l=list(di.values())
        l.sort(key=lambda x:x[0][1])
        for i in range(len(l)):
            l[i].sort(key=lambda x:(x[0],x[2]))
            l[i]=[j[2] for j in l[i]]
        return l
'''
