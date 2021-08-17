#attempt1: Remember you only need t maintain maxvalue till here and not the sorted
#list
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def recurse(root,maxtillhere):
            if not(root):
                return 0
            ans=recurse(root.left,max(root.val,maxtillhere))+recurse(root.right,max(root.val,maxtillhere))
            if root.val>=maxtillhere:
                #print(root.val,maxtillhere)
                return ans+1
            return ans
        return recurse(root,-float('inf'))
        