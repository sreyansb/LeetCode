#1st attempt->95% speed
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,indexx,indexy,dic):
    if root:
        if indexx not in dic:
            dic[indexx]=[]
        dic[indexx].append((root.val,indexy))
        helper(root.left,indexx-1,indexy-1,dic)
        helper(root.right,indexx+1,indexy-1,dic)

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic={}
        k=helper(root,0,0,dic)
        j=sorted(dic.keys())
        l=[]
        for k in j:
            m=sorted(dic[k],key=lambda x:(-x[1],x[0]))
            x=[]
            for n in m:
               x.append(n[0])
            l.append(x)                  
        return l
        
