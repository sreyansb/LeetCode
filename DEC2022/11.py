#attempt4:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxAns = [-float('inf')]
        #findAns returns (left+node,node,right+node)
        def findAns(node):
            if node:
                leftNodeAns = findAns(node.left)
                rightNodeAns = findAns(node.right)
                maxAns[0] = max(
                    maxAns[0], node.val,
                    node.val + max(leftNodeAns),
                    node.val + max(rightNodeAns),
                    node.val + max(leftNodeAns) + max(rightNodeAns)
                )
                return (node.val+max(leftNodeAns),node.val,node.val+max(rightNodeAns))
            return (-float(inf), -float('inf'), -float('inf'))
        findAns(root)
        return maxAns[0]

#attempt3: WA because I didn't understand the question. We need to have
# a path and not just subtree sum
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #node, node+right, node+left, node+right+left, right, left
        def findAns(node):
            if node:
                rightTreeVal, rightNodeTaken = findAns(node.right)
                leftTreeVal, leftNodeTaken = findAns(node.left)
                combinedSum = node.val
                newRightVal = node.val
                newLeftVal = node.val
                if rightNodeTaken:
                    newRightVal += rightTreeVal
                    combinedSum += rightTreeVal
                if leftNodeTaken:
                    newLeftVal += leftTreeVal
                    combinedSum += leftTreeVal
                return max(
                    [
                        (node.val,True), (newRightVal, True), (newLeftVal, True), (combinedSum, True), (rightTreeVal, False), (leftTreeVal, False)
                    ],
                    key = lambda x:x[0]
                    )
            return (-float('inf'),True)
        
        return findAns(root)[0]
'''

#attempt2: WA what if leftnode's ans doesn't include itself
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #node, node+right, node+left, node+right+left, right, left
        def findAns(node):
            if node:
                rightTreeAns = findAns(node.right)
                leftTreeAns = findAns(node.left)
                return max(node.val, node.val+rightTreeAns, node.val+leftTreeAns, node.val+rightTreeAns+leftTreeAns, rightTreeAns, leftTreeAns)
            return -float('inf')
        
        return findAns(root)
'''

#attempt1: WA What about sngle node tree?!
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #node, node+right, node+left, node+right+left, right, left
        def findAns(node):
            if node:
                rightTreeAns = findAns(node.right)
                leftTreeAns = findAns(node.left)
                return max(node.val, node.val+rightTreeAns, node.val+leftTreeAns, node.val+rightTreeAns+leftTreeAns, rightTreeAns, leftTreeAns)
            return 0
        
        return findAns(root)
'''
