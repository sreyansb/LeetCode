#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildtree(start_inorder_index,end_inorder_index,preorder):
            if not(preorder) or start_inorder_index>end_inorder_index:
                return None
            number_at_head = preorder.pop(0)
            node = TreeNode(number_at_head)
            index_in_inorder = inorder.index(number_at_head)
            node.left = buildtree(start_inorder_index,index_in_inorder-1,preorder)
            node.right = buildtree(index_in_inorder+1,end_inorder_index,preorder)
            return node
        return buildtree(0,len(inorder)-1,preorder)
        
