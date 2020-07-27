#2nd Attempt
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not(inorder):
            return None
        allindices={inorder[i]:i for i in range(len(inorder))}
        def building(l,r):
            if l>r:
                return None
            vertex=postorder.pop()
            indexofvertex=allindices[vertex]
            k=TreeNode(vertex)
            k.right=building(indexofvertex+1,r)
            k.left=building(l,indexofvertex-1)
            return k
        return building(0,len(postorder)-1)
#1st attempt
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def buildtree(ino,po,start,end,nodebase):
    if start>end:
        return None
    k=TreeNode(po[nodebase[-1]])
    nodebase[-1]-=1
    #print(k.val)
    indexinino=start+ino[start:end+1].index(k.val)
    k.right=buildtree(ino,po,indexinino+1,end,nodebase)
    k.left=buildtree(ino,po,start,indexinino-1,nodebase)
    return k

class Solution:
    def buildTree(self, inorder,postorder) -> TreeNode:
        listy=[len(postorder)-1]
        head=buildtree(inorder,postorder,0,len(postorder)-1,listy)
        return head
"""
ino=[9,3,15,20,7]
po=[9,15,7,20,3]
obj=Solution()
print(obj.buildTree(ino,po))
