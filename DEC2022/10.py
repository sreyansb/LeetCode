#attempt3:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def sumBinaryTree(root):
            if root:
                root.val += sumBinaryTree(root.left) + sumBinaryTree(root.right)
                return root.val
            return 0
        
        sumBinaryTree(root)
        maxAns = [-float('inf')]

        def findMaxAns(summedRoot, ancestralSum):
            if summedRoot:
                leftRootSummedVal = summedRoot.left.val if summedRoot.left else 0
                rightRootSummedVal = summedRoot.right.val if summedRoot.right else 0
                maxAns[0] = max(maxAns[0], (summedRoot.val+ancestralSum-leftRootSummedVal)*(leftRootSummedVal), (summedRoot.val+ancestralSum-rightRootSummedVal)*(rightRootSummedVal))
                findMaxAns(summedRoot.left, ancestralSum + summedRoot.val - leftRootSummedVal)
                findMaxAns(summedRoot.right, ancestralSum + summedRoot.val - rightRootSummedVal)
        findMaxAns(root, 0)
        return maxAns[0]%(1000000007)

#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def sumBinaryTree(root):
            newRoot = TreeNode(val = 0)
            if root:
                root.val += sumBinaryTree(root.left) + sumBinaryTree(root.right)
                return root.val
            return 0
        
        sumBinaryTree(root)
        maxAns = [-float('inf')]
        
        def findMaxAns(summedRoot, ancestralSum):
            if summedRoot:
                leftRootSummedVal = summedRoot.left.val if summedRoot.left else 0
                rightRootSummedVal = summedRoot.right.val if summedRoot.right else 0
                maxAns[0] = max(maxAns[0], (summedRoot.val+ancestralSum-leftRootSummedVal)*(leftRootSummedVal), (summedRoot.val+ancestralSum-rightRootSummedVal)*(rightRootSummedVal))
                findMaxAns(summedRoot.left, ancestralSum + summedRoot.val - leftRootSummedVal)
                findMaxAns(summedRoot.right, ancestralSum + summedRoot.val - rightRootSummedVal)
        findMaxAns(root, 0)
        return maxAns[0]%(1000000007)

#attempt1: Really slow

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def sumBinaryTree(root):
            newRoot = TreeNode(val = 0)
            if root:
                leftRoot = sumBinaryTree(root.left)
                rightRoot = sumBinaryTree(root.right)
                newRoot.left = leftRoot
                newRoot.right = rightRoot
                newRoot.val = root.val + leftRoot.val + rightRoot.val
            return newRoot
        
        summedRoot = sumBinaryTree(root)
        maxAns = [-float('inf')]
        def findMaxAns(summedRoot, ancestralSum):
            if summedRoot:
                leftRootSummedVal = summedRoot.left.val if summedRoot.left else 0
                rightRootSummedVal = summedRoot.right.val if summedRoot.right else 0
                maxAns[0] = max(maxAns[0], (summedRoot.val+ancestralSum-leftRootSummedVal)*(leftRootSummedVal), (summedRoot.val+ancestralSum-rightRootSummedVal)*(rightRootSummedVal))
                findMaxAns(summedRoot.left, ancestralSum + summedRoot.val - leftRootSummedVal)
                findMaxAns(summedRoot.right, ancestralSum + summedRoot.val - rightRootSummedVal)
        findMaxAns(summedRoot, 0)
        return maxAns[0]%(1000000007)
