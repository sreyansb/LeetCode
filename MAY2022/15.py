#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while(True):
            newqueue = []
            for node in queue:
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            if not(newqueue):
                break
            queue = newqueue
        return sum([node.val for node in queue])
        
