#attempt1: 61%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not(root):
            return 0
        def finddiff(root,maxi,mini):
            t1=()
            t2=()
            if root.left:
                t1=finddiff(root.left,max(maxi,root.left.val),min(mini,root.left.val))
            if root.right:
                t2=finddiff(root.right,max(maxi,root.right.val),min(mini,root.right.val))
            maxi1,mini1,mini2,maxi2=root.val,root.val,root.val,root.val
            if t1:
                maxi1=max(maxi,t1[0])
                mini1=min(mini,t1[1])
            if t2:
                maxi2=max(maxi,t2[0])
                mini2=min(mini,t2[1])
            print(root.val,t1,t2)
            if (maxi2-mini2)>(maxi1-mini1):
                return (maxi2,mini2)
            else:
                return (maxi1,mini1)
        t1=finddiff(root,root.val,root.val)
        #print(t1)
        return abs(t1[0]-t1[1])
        
            
        
