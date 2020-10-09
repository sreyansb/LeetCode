#attempt1: We convert the given *BST* to preorder and then construct the tree
#using inorder and preorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root: TreeNode) -> str:
        #it is a binary search tree and hence inorder will be sorted.
        #therefore we can store in preorder.
        arr=[]
        def preorder(root):
            if root:
                arr.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return str(arr)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data=="[]":
            return None
        data=data[1:-1]
        preorder=[int(i.strip()) for i in data.split(",")]
        inorder=sorted(preorder)
        n=len(inorder)
        
        def createtree(start,end,nodes):
            if start>end:
                return None
            k=TreeNode(preorder[nodes[0]])
            indexinorder=inorder.index(preorder[nodes[0]])
            nodes[0]+=1
            k.left = createtree(start,indexinorder-1,nodes)
            k.right = createtree(indexinorder+1,end,nodes)
            return k
            
        return createtree(0,n-1,[0])
