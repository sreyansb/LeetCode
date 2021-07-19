#attempt2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(curnode,pval,qval):
            if not(curnode):
                return None
            if pval<curnode.val<qval:
                return curnode
            if curnode.val in (pval,qval):
                return curnode
            rightanswer=lca(curnode.right,pval,qval)
            leftanswer=lca(curnode.left,pval,qval)
            return leftanswer or rightanswer
        return lca(root,min(p.val,q.val),max(p.val,q.val))

#attempt1:WA assumed that p and q will be sorted
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(curnode,pval,qval):
            if not(curnode):
                return None
            if pval<curnode.val<qval:
                return curnode
            if curnode.val in (pval,qval):
                return curnode
            rightanswer=lca(curnode.right,pval,qval)
            leftanswer=lca(curnode.left,pval,qval)
            return leftanswer or rightanswer
        return lca(root,p.val,q.val)
'''