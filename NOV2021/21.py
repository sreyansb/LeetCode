#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        postorderindex = [n]
        def construct(start,end):
            if start>end or postorderindex[-1]<0:
                return None
            postorderindex[-1] -= 1
            nodeval = postorder[postorderindex[-1]]
            indexinorder = inorder.index(nodeval)
            node = TreeNode(nodeval)
            node.right = construct(indexinorder+1,end)
            node.left = construct(start,indexinorder-1)
            return node
        return construct(0,n-1)
