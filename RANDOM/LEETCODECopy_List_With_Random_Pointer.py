#attempt1:
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not(head):
            return None
        headc=head
        random=[]
        nodes=[]
        di={}
        while(headc):
            copy=Node(headc.val)
            di[headc]=copy
            nodes.append(copy)
            if headc.random:
                random.append(headc.random)
            else:
                random.append(-1)
            headc=headc.next
        last=None
        for i in range(len(nodes)-1):
            nodes[i].next=nodes[i+1]
            if random[i]!=-1:
                nodes[i].random=di[random[i]]
            else:
                nodes[i].random=last
        #print(di)
        if random[-1]!=-1:
            nodes[-1].random=di[random[-1]]
        else:
            nodes[-1].random=last
        return nodes[0]
        
        
        
        
        
