#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(low,high):
            if low>high:
                return None
            mid = (low+high)//2
            tree = TreeNode(nums[mid])
            tree.left = createTree(low,mid-1)
            tree.right = createTree(mid+1,high)
            return tree
        return createTree(0,len(nums)-1)
        
