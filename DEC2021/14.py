#attempt2: 200ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def eachnode(root):
            if root:
                if low<=root.val<=high:
                    ans[0] += root.val
                if root.val>=low:
                    eachnode(root.left)
                if root.val<=high:
                    eachnode(root.right)
        eachnode(root)
        return ans[0]                
        

#attempt1: 284ms
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def eachnode(root):
            if root:
                if low<=root.val<=high:
                    ans[0] += root.val
                eachnode(root.left)
                eachnode(root.right)
        eachnode(root)
        return ans[0]                
'''
