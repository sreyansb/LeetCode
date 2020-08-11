# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        stack=[]
        if not(root):
            return stack
        curlevel=[root]
        while(curlevel):
            while(curlevel and curlevel[-1]==None):
                curlevel.pop()
            copyy=[]
            if curlevel:
                k=curlevel.pop()
                stack.append(k.val)
                if k:
                    copyy.append(k.right)
                    copyy.append(k.left)
            while(curlevel):
                k=curlevel.pop()
                if k:
                    copyy.append(k.right)
                    copyy.append(k.left)
            curlevel=copyy[::-1]
            
        return stack
        
