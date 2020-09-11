"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not(root):
            return []
        current=[root]
        ans=[]
        while(current):
            nextlevel=[]
            curans=[]
            index=0
            while(index<len(current)):
                curans.append(current[index].val)
                for i in current[index].children:
                    if i!=None:
                        nextlevel.append(i)
                index+=1
            current=nextlevel.copy()
            ans.append(curans)
        return ans
            
        
