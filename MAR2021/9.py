#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d==1:
            newn=TreeNode(v)
            newn.left=root
            return newn
        curlevel=[root]
        d-=2
        while(d):
            newlevel=[]
            for i in curlevel:
                if i.left:
                    newlevel.append(i.left)
                if i.right:
                    newlevel.append(i.right)
            curlevel=newlevel.copy()
            del newlevel
            d-=1
        for i in curlevel:
            temp1,temp2=i.left,i.right
            i.left,i.right=TreeNode(v),TreeNode(v)
            i.left.left=temp1
            i.right.right=temp2
        return root
