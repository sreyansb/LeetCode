#attempt1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        def inorder(root,arr):
            if root:
                inorder(root.left,arr)
                arr.append(root.val)
                inorder(root.right,arr)
        inorder(root,self.arr)
        self.index = 0
        self.limit = len(self.arr)    
    

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index-1]

    def hasNext(self) -> bool:
        return self.index<self.limit
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
