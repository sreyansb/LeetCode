#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans=[]
        def pathsum(curnode,visited,cursum):
            if not(curnode):
                return 
            #print(curnode.val)
            if not(curnode.left) and not(curnode.right):
                if curnode.val+cursum==target:
                    ans.append((visited+[curnode.val]).copy())
                return
            else:
                pathsum(curnode.left,visited+[curnode.val],cursum+curnode.val)
                pathsum(curnode.right,visited+[curnode.val],cursum+curnode.val)
        pathsum(root,[],0)
        return ans
                