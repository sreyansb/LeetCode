#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = deque([(root,0)])
        while(queue):
            #print([i[-1] for i in queue])
            ans = max(ans,queue[-1][-1]-queue[0][-1]+1)
            newqueue = deque([])
            for node,index in queue:
                if node:
                    newqueue.append((node.left,2*index+1))
                    newqueue.append((node.right,2*index+2))
            while(newqueue and not newqueue[-1][0]):
                newqueue.pop()
            while(newqueue and not newqueue[0][0]):
                newqueue.popleft()
            queue = newqueue
        return ans

#attempt1: WA because din't take into consideration the phrasing of the question
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        queue = deque([root])
        while(queue):
            ans = max(ans,len(queue))
            newqueue = deque([])
            for node in queue:
                if node:
                    newqueue.append(node.left)
                    newqueue.append(node.right)
            while(newqueue and not newqueue[-1]):
                newqueue.pop()
            while(newqueue and not newqueue[0]):
                newqueue.popleft()
            queue = newqueue
        return ans
'''
