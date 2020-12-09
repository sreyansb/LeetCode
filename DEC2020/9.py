#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root,arr):
        if root:
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.index=-1
        self.inorderl=[]
        inorder(root,self.inorderl)
        self.leng=len(self.inorderl)
        
    def next(self) -> int:
        if self.index+1<self.leng:
            self.index+=1
            return self.inorderl[self.index]
        
    def hasNext(self) -> bool:
        return self.index+1<self.leng
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
