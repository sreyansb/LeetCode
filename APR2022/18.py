#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numbers = []
        def inorder(root):
            if root:
                inorder(root.left)
                numbers.append(root.val)
                inorder(root.right)
        inorder(root)
        return numbers[k-1]
                
        
