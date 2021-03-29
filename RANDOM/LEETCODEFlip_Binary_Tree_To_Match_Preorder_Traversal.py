#attempt1: TOOK HELP very important problem
#Very important logic to have global index
#this global index holds the index to voyage
#you check the value in voyage[index] and root.val, if different=>Cant be changed
#always left child is 1 index away from parent child in Preorder traversal
#Then we check root.left's val, if different optimistically swap
#in the next iteration, without incrementing i, just check and continue
#if you swap with wrong value, will be caught in root.val!=voyage[index]
#What I thought was to make a similar thing but couldn't actually implement it

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        i=[0]
        ans=[]
        def check(root):
            if not root:
                return True
            if root.val!=voyage[i[0]]:
                return False
            i[0]+=1
            if root.left and root.left.val!=voyage[i[0]]:
                ans.append(root.val)
                root.left,root.right=root.right,root.left
            return check(root.left) and check(root.right)
        if check(root):
            return ans
        return [-1]
        
        
