#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        level = [root]
        while(level):
            currentSum = 0
            totalCount = 0
            nextLevel = []
            for root in level:
                currentSum += root.val
                totalCount += 1
                if root.left:
                    nextLevel.append(root.left)
                if root.right:
                    nextLevel.append(root.right)
            level = nextLevel
            ans.append(currentSum/totalCount)
        return ans
        
