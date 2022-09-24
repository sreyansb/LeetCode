#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def findSum(curRoot,curSum=0,values=[]):
            if curRoot:
                if not(curRoot.left) and not(curRoot.right):
                    values += [curRoot.val]
                    curSum += curRoot.val
                    if curSum == targetSum:
                        ans.append(values)
                    return
                findSum(curRoot.left,curSum+curRoot.val,values+[curRoot.val])
                findSum(curRoot.right,curSum+curRoot.val,values+[curRoot.val])
        findSum(root,0)
        return ans
