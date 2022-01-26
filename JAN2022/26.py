#attempt1: Merge SOrt algo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = []
        l2 = []
        
        def inorder(root,l):
            if root:
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)
        
        inorder(root1,l1)
        inorder(root2,l2)
        l1len = len(l1)
        l2len = len(l2)
        i,j = 0,0
        final = []
        while(i<l1len and j<l2len):
            if l1[i]<l2[j]:
                final.append(l1[i])
                i += 1
            else:
                final.append(l2[j])
                j += 1
        while(i<l1len):
            final.append(l1[i])
            i += 1
        while(j<l2len):
            final.append(l2[j])
            j += 1
        return final
            
        
