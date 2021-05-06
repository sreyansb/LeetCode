#attempt1:
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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodes=[]
        while(head):
            nodes.append(TreeNode(head.val))
            head=head.next
        def check(start,end):
            if start>end:
                return
            mid=(start+end)//2
            nodes[mid].left=check(start,mid-1)
            nodes[mid].right=check(mid+1,end)
            return nodes[mid]
        return check(0,len(nodes)-1)
            
        
