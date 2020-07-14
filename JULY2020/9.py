class Treenode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        maxie=1
        curlevel=[root]
        while(curlevel):
            nextlevel=[]
            no=0
            for i in range(len(curlevel)-1,-1,-1):
                if curlevel[i] is None:
                    no+=1
                else:
                    for j in range(i+1):
                        if curlevel[j] is not None:
                            nextlevel.append(curlevel[j].left)
                            nextlevel.append(curlevel[j].right)
                        else:
                            nextlevel.append(None)
                            nextlevel.append(None)
                    break
            
            maxie=max(maxie,len(curlevel)-no)
            i=0
            while(i<len(nextlevel) and nextlevel[i]==None):
                i+=1
                
            curlevel=nextlevel[i:]
            #print(maxie)
            
        return maxie

root=Treenode()
root1=Treenode()
root2=Treenode()
root3=Treenode()
root4=Treenode()
root5=Treenode()
root6=Treenode()

root.val=1
root1.val=1
root2.val=1
root3.val=1
root4.val=1
root5.val=1
root6.val=1

root.left=root1
root.right=root2
root1.left=root3
root2.right=root4
root3.left=root5
root4.right=root6
obj=Solution()
print(obj.widthOfBinaryTree(root))
