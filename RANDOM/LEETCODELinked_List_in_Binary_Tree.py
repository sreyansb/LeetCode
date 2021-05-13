#attempt2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        ans=[]
        
        def check_current(root,curpath):
            if not(root.left) and not(root.right):
                curpath=curpath+[root.val]
                ans.append(curpath.copy())
            if root.left:
                check_current(root.left,curpath+[root.val])
            if root.right:
                check_current(root.right,curpath+[root.val])
        check_current(root,[])
        fin=[]
        while(head):
            fin.append(head.val)
            head=head.next
        n=len(fin)
        #print(ans)
        #print(fin)
        for i in ans:
            if len(i)<n:
                continue
            for j in range(len(i)-n+1):
                flag=1
                for k in range(n):
                    if i[j+k]!=fin[k]:
                        flag=0
                        break
                if flag:
                    return True
        return False

#attempt1:
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def check_current(root,headc):
            
            if not(headc):
                return True
            
            if not(root):
                return False
            
            if root.val==headc.val:
                
                ans=False
                ans=ans or check_current(root.left,headc.next)
                if ans:
                    return ans
                ans=ans or check_current(root.right,headc.next)
                return ans
            else:
                return False or check_current(root.left,head) or check_current(root.right,head)
        
        return check_current(root,head)
'''
