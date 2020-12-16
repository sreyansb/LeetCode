#attempt2: Check Inorder and find that they return sorted order and
#len(set(ans))=len(set)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans=[]
        def recurse(head):
            if head:
                recurse(head.left)
                ans.append(head.val)
                recurse(head.right)
        recurse(root)
        if ans==sorted(ans) and len(ans)==len(set(ans)):
            return True
        return False

#attempt1: It will give locally optimal solution and hence wont work for
#[5,4,6,null,null,3,7] because 3 is less than 6 but not greater than 5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recurse(head):
            if head:
                if head.left:
                    if head.left.val>=head.val:
                        return False
                if head.right:
                    if head.right.val<=head.val:
                        return False
                return True and recurse(head.left) and recurse(head.right)
            return True
        return recurse(root)
'''                       
        
