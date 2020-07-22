# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        else:
            le=0
            cur=[root]
            k=[]
            while(cur):
                nw=[]
                nextl=[]
                for i in cur:
                    nw.append(i.val)
                    if i.left:
                        nextl.append(i.left)
                    if i.right:
                        nextl.append(i.right)
                if le==0:
                    k.append(nw)
                else:
                    k.append(nw[::-1])#nw.reverse() is slower
                cur=nextl
                le^=1
            return k
                        
                    
                
            
        
