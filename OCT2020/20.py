#Attempt1: 99% very nice problem, get the number of nodes,
#since the values are from 1 to len(graph), we can get the relationships
#using noderela, use that and create the new graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not(node):
            return None
        noderela={}
        def ldfs(i,visited):
            if i.val in visited:
                return 0
            visited.append(i.val)
            noderela[i.val]=set()
            for j in i.neighbors:
                ldfs(j,visited)
                noderela[i.val].add(j.val)
        visited=[]
        ldfs(node,visited)
        k=len(visited)
        nodelist=[Node(i) for i in range(k+1)]
        for j in noderela:
            for k in noderela[j]:
                nodelist[j].neighbors.append(nodelist[k])
        return nodelist[1]
        
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node4.neighbors.append(node1)
node3.neighbors.append(node2)
node3.neighbors.append(node4)
node2.neighbors.append(node3)
node4.neighbors.append(node3)
obj=Solution()
obj.cloneGraph(node1)
