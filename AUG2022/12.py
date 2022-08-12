#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCS(currentRoot,minVal,maxVal):
            if currentRoot:
                if minVal<=currentRoot.val<=maxVal:
                    return currentRoot
                if maxVal<currentRoot.val:
                    return findLCS(currentRoot.left,minVal,maxVal)
                return findLCS(currentRoot.right,minVal,maxVal)
            return None
        return findLCS(root,min(p.val,q.val),max(p.val,q.val))
        

#attempt1: RUNTIME error bcoz I used root instead of currentRoot
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCS(currentRoot,minVal,maxVal):
            if currentRoot:
                if minVal<=currentRoot.val<=maxVal:
                    return currentRoot
                if maxVal<currentRoot.val:
                    return findLCS(root.left,minVal,maxVal)
                return findLCS(root.right,minVal,maxVal)
            return None
        return findLCS(root,min(p.val,q.val),max(p.val,q.val))
        
'''
