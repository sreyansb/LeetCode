# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def findfunction(p,st):
    if p==None or (p.left==None and p.right==None):
        return
    else:
        if p.left==None:
            st.append(None)
        elif p.left:
            st.append(p.left.val)
        if p.right==None:
            st.append(None)
        elif p.right:
            st.append(p.right.val)
        findfunction(p.left,st)
        findfunction(p.right,st)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None) :
            return False
        else:
            st1=[p.val]
            st2=[q.val]
            findfunction(p,st1)
            findfunction(q,st2)
            return True if st1==st2 else False
            
        
