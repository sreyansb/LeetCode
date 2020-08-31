def inorder(k):
        while(k.left!=None):
            k=k.left
        return k
    
#important for when we have only left child.
#so we need to take the largest of them.
    
def inorder1(k):
    while(k.right!=None):
            k=k.right
    return k
        
def delete(root,key):
    if root:
        if root.val==key:
            if not(root.left) and not(root.right):
                return None
            if root.right:
                    j=inorder(root.right)
                    root.val=j.val
                    root.right=delete(root.right,j.val)
                    return root
            else:
                    j=inorder1(root.left)
                    root.val=j.val
                    root.left=delete(root.left,j.val)
                    return root
        elif root.val<key:
            root.right=delete(root.right,key)
            return root
        else:
            root.left=delete(root.left,key)
            return root
    return None
                
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        root=delete(root,key)
        return root
