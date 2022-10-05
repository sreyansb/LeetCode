#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val = val, left = root)
        queue = [root]
        for dep in range(1,depth-1):
            nextQueue = []
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            queue = nextQueue
        for node in queue:
            newLeftNode = TreeNode(val,left = node.left)
            newRightNode = TreeNode(val,right = node.right)
            node.left = newLeftNode
            node.right = newRightNode
        return root
