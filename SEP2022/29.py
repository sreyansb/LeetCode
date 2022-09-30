#attempt1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def find_len_of_list(cur_node):
            if cur_node:
                return 1 + find_len_of_list(cur_node.next)
            return 0
        
        len_of_list = find_len_of_list(head)
        headc = head
        parent = None
        for loop_through in range(len_of_list-n):
            parent = headc
            headc = headc.next
        if parent == None:
            return head.next
        parent.next = headc.next
        return head
