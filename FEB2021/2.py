#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        rootc=root
        def trim(root):
            if root:
                if root.val<low:
                    return trim(root.right)
                elif root.val>high:
                    return trim(root.left)
                else:
                    root.right=trim(root.right)
                    root.left=trim(root.left)
                    return root
            else:
                return None
        return trim(root)
                
#attempt1: thought that this was quite difficult

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        rootc=root
        def trim(root):
            if root:
                if root.val<low:
                    root.left=None
                    root.right=trim(root.right)
                    return root.right
                elif root.val>high:
                    root.right=None
                    root.left=trim(root.left)
                    return root.left
                else:
                    root.right=trim(root.right)
                    root.left=trim(root.left)
                    return root
            else:
                return root
        return trim(root)
'''
                
        
