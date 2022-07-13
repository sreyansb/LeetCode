#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not(root):
            return []
        ans = []
        queue = [root]
        while(queue):
            nextqueue = []
            ans.append([])
            for node in queue:
                ans[-1].append(node.val)
                if node.left:
                    nextqueue.append(node.left)
                if node.right:
                    nextqueue.append(node.right)
            queue = nextqueue
        return ans
