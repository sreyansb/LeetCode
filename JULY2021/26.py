#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def merge(low,high):
            if low>high:
                return None
            mid=low+(high-low)//2
            curnode=TreeNode(nums[mid])
            curnode.left=merge(low,mid-1)
            curnode.right=merge(mid+1,high)
            return curnode
        return merge(0,len(nums)-1)
        