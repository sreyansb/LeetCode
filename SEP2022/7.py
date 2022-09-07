#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preOrder(root):
            if root:
                leftString = preOrder(root.left)
                rightString = preOrder(root.right)
                if rightString == "()":
                    rightString = ""
                if leftString == "()" and rightString=="":
                    leftString = ""
                return f"({root.val}{leftString}{rightString})"
                
            return "()"
        return preOrder(root)[1:-1]
        
