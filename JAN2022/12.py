#attempt2: 182ms because of context switch
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(curroot,tobeinserted):
            parent = None
            while(curroot):
                parent = curroot
                if curroot.val>val:
                    curroot = curroot.left
                else:
                    curroot = curroot.right
            if parent.val>val:
                parent.left = tobeinserted
            else:
                parent.right = tobeinserted                    
        
        if not(root):
            return TreeNode(val)
        insert(root,TreeNode(val))
        return root
            
        

#attempt1: Like an idiot:coded deletion
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def find(curroot,curval):
            if curroot:
                if curroot.val == curval:
                    if not(curroot.left) and not(curroot.right):
                        return None
                    elif not(curroot.right):
                        new = curroot.left
                        while(new.right):#finding next inorder successor in the left subtree
                            new = new.right
                        curroot.val = new.val
                        curroot.right = find(curroot.right,new.val)
                    else:
                        new = curroot.right
                        while(new.left):#finding next inorder successor in the left subtree
                            new = new.left
                        curroot.val = new.val
                        curroot.left = find(curroot.left,new.val)
                else:
                    if curroot.val<curval:
                        curroot.right = find(curroot.right,curval)
                    else:
                        curroot.left = find(curroot.left,curval)
            return curroot
        
        return find(root,val)
            
        
'''
