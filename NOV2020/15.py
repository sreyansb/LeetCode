#attempt1: 97% and 63%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def calculate(root,sumc):
            if root:
                if root.val<low:
                    calculate(root.right,sumc)
                elif root.val>high:
                    calculate(root.left,sumc)
                else:
                    sumc[0]+=root.val
                    calculate(root.left,sumc)
                    calculate(root.right,sumc)
        sumc=[0]
        calculate(root,sumc)
        return sumc[0]
                
        
