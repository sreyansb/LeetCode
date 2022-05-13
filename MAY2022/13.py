#attempt1:
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not(root):
            return root
        all_nodes_in_a_level = [root]
        while(all_nodes_in_a_level):
            next_level = []
            for i in range(len(all_nodes_in_a_level)-1):
                all_nodes_in_a_level[i].next = all_nodes_in_a_level[i+1]
                if all_nodes_in_a_level[i].left:
                    next_level.append(all_nodes_in_a_level[i].left)
                if all_nodes_in_a_level[i].right:
                    next_level.append(all_nodes_in_a_level[i].right)
            if all_nodes_in_a_level[-1].left:
                    next_level.append(all_nodes_in_a_level[-1].left)
            if all_nodes_in_a_level[-1].right:
                    next_level.append(all_nodes_in_a_level[-1].right)
            all_nodes_in_a_level = next_level
        return root
                
            
        
