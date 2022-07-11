#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not(root):
            return []
        queue = [root]
        ans = []
        while(queue):
            ans.append(queue[-1].val)
            newqueue = []
            for node in queue:
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            queue = newqueue
        return ans
