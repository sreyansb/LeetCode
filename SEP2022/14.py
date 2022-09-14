#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def checkCount(curPath):
            oddOccur = 0
            for ele in curPath:
                if curPath[ele]&1:
                    oddOccur += 1
            return oddOccur <= 1
        
        def addToPath(val,curPath):
            if val not in curPath:
                curPath[val] = 0
            curPath[val] += 1
            
        def countPaths(root,curPath):
            if root:
                addToPath(root.val,curPath)
                ans = 0
                if not(root.left) and not(root.right):
                    if checkCount(curPath):
                        ans = 1
                else:
                    ans = countPaths(root.left,curPath) + countPaths(root.right,curPath)
                curPath[root.val] -= 1
                return ans
            return 0
        
        return countPaths(root,{})
