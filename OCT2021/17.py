#attempt2: AC : code is that we use prefix sum
# and at every node using this current node we check if targetSum can be made
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        ans = [0]
        def pathsum(node,curlist):
            if not (node):
                return
            curlist.append(curlist[-1]+node.val)
            n = len(curlist)
            for i in range(n-1):
                if curlist[-1]-curlist[i] == targetSum:
                    ans[0] += 1
            pathsum(node.left,curlist)
            pathsum(node.right,curlist)
            curlist.pop()
        pathsum(root,[0])
        return ans[0]

#attempt1: WRONG IDEA BECAUSE AT END NODES HAVING SAME PARENTAGE
# ANSWERS WILL BE EVALUATED TWICE
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        ans = [0]
        def pathsum(node,curlist):
            if not (node):
                n = len(curlist)
                for i in range(1,n):
                    if curlist[i] == targetSum:
                        ans[0] += 1
                    for j in range(i+1,n):
                        if curlist[j]-curlist[i] == targetSum:
                            ans[0] += 1
                return
            pathsum(node.left,curlist+[curlist[-1]+node.val])
            pathsum(node.right,curlist+[curlist[-1]+node.val])
'''
  