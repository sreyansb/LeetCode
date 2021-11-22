#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delandsearch(root,key):
            if root:
                val = root.val
                if val == key:
                    if root.left:
                        newhead = root.left
                        while(newhead.right):
                            newhead = newhead.right
                        root.val = newhead.val
                        root.left = delandsearch(root.left,newhead.val)
                    elif root.right:
                        newhead = root.right
                        while(newhead.left):
                            newhead = newhead.left
                        root.val = newhead.val
                        root.right = delandsearch(root.right,newhead.val)
                    else:
                        return None
                    return root
                else:
                    root.left = delandsearch(root.left,key)
                    root.right = delandsearch(root.right,key)
                    return root
            return None
        return delandsearch(root,key)
                        
                        
