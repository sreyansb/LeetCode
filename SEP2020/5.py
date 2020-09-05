#ATTEMPT2 - 92%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        finallist=[]
        def inorder(root,l):
            if root:
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)
                
        inorder(root1,finallist)
        inorder(root2,finallist)
        return sorted(finallist)
        
        

#Attempt1 - 70%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=[]
        list2=[]
        finallist=[]
        def inorder(root,l):
            if root:
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)
                
        inorder(root1,list1)
        inorder(root2,list2)
        l1=len(list1)
        l2=len(list2)
        i=0
        j=0
        while(i<l1 and j<l2):
            if list1[i]<list2[j]:
                finallist.append(list1[i])
                i+=1
            elif list1[i]>list2[j]:
                finallist.append(list2[j])
                j+=1
            else:
                finallist.append(list2[j])
                finallist.append(list1[i])
                j+=1
                i+=1
        while(i<l1):
            finallist.append(list1[i])
            i+=1
        while(j<l2):
            finallist.append(list2[j])
            j+=1
        return finallist
"""
