#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def find(root):
            if root:
                s.add(root.val)
                find(root.left)
                find(root.right)
        find(root)
        for ele in s:
            if k-ele in s and k-ele != ele:
                return True
        return False

#attempt1: WA because didn't take care of k-ele == ele
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def find(root):
            if root:
                s.add(root.val)
                find(root.left)
                find(root.right)
        find(root)
        for ele in s:
            if k-ele in s:
                return True
        return False
'''
