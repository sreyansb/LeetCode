#attempt1: Similar to Postorder to BST conversion except that vertex exists at
# start of the array

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        n = len(inorder)
        if n == 0:
            return None
        curindex = [0]
        
        def create(start,end):
            if start>end:
                return None
            ele = preorder[curindex[0]]
            curindex[0] += 1
            posinorder = inorder.index(ele)
            root = TreeNode(ele)
            root.left = create(start,posinorder-1)
            root.right = create(posinorder+1,end)
            return root
        return create(0,n-1)
            
        