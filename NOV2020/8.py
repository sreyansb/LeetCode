#aattempt3: took help, made a nice code in attempt2 but gave WA
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
class Solution:
    def findTilt(self, root: TreeNode) -> int: 
        ans=[0]
        def preorder(root):
            if not(root):
                return 0
            if root:
                l,r=0,0
                l=preorder(root.left)
                r=preorder(root.right)
                ans[0]+=abs(l-r)
                return l+r+root.val
                
        preorder(root)
        return ans[-1]
                
                
        
        
        
        
