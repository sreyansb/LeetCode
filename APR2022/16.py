#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def BST_convertor_sum_generator(root): #returns leftsubtreesum,rootval,rightsubtreesum
            if root:
                return root.val+BST_convertor_sum_generator(root.left)+BST_convertor_sum_generator(root.right)
            return 0
        
        def BST_convertor_changer(root,parent_val=0):
            if root:
                rightsubtreesum = BST_convertor_sum_generator(root.right)
                BST_convertor_changer(root.right,parent_val)
                root.val += rightsubtreesum + parent_val
                BST_convertor_changer(root.left,root.val)
            return root
        
        return BST_convertor_changer(root)
                
                
                
                
