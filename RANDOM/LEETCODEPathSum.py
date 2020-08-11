# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def hasPathSum(self, root, sum):
        if root:
            print(root.val,sum)
            if root.left==None and root.right==None and sum==root.val:#sum==0 wrong hai
                return True
            if root.left==None and root.right==None and sum!=root.val:
                return False
            return (self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val))
        else:
            return False

obj=Solution()
root=TreeNode()
root.val=5

root1=TreeNode()
root1.val=4

root2=TreeNode()
root2.val=8

root3=TreeNode()
root3.val=11

root4=TreeNode()
root4.val=7

root5=TreeNode()
root5.val=2

root6=TreeNode()
root6.val=13

root7=TreeNode()
root7.val=4

root8=TreeNode()
root8.val=1

root.left=root1
root.right=root2
root1.left=root3
root3.left=root4
root3.right=root5
root2.left=root6
root2.right=root7
root7.right=root8
print(obj.hasPathSum(root,22))

