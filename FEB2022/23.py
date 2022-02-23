#attempt1:
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not(node):
            return None
        di = {}
        queue = [node]
        visited = {node.val}
        di[node.val] = []
        #initval = node.val
        while(queue):
            newqueue = []
            for node in queue:
                for i in node.neighbors:
                    if i.val not in visited:
                        newqueue.append(i)
                        di[i.val] = []
                        visited.add(i.val)
                    di[node.val].append(i.val)
            queue = newqueue
        maxnode = max(di)
        newdi = {}
        for i in di:
            newdi[i] = Node(i)
        for i in di:
            for neighbourval in di[i]:
                #print(i,neighbourval)
                newdi[i].neighbors.append(newdi[neighbourval])
        #print(newdi)
        return newdi[1]
        
        
        
            
        
