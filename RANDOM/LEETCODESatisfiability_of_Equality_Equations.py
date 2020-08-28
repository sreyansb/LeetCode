#Accepted code. Thought of this approach but skeptical about its performance
#Attempt2
def find(graph,va,vb,visited):
    if va==vb:
        return True
    if va in visited:
        return False
    visited.add(va)
    k=False
    for i in graph[va]:
        if i==vb:
            k=True
            return True
        k =k| find(graph,i,vb,visited)
    return k
    
    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations.sort(key=lambda x:x[1],reverse=True)
        graph=[[] for i in range(26)]
        for i in equations:
            if i[1]=="=":
                graph[ord(i[0])-97].append(ord(i[3])-97)
                graph[ord(i[3])-97].append(ord(i[0])-97)
            else:
                k=find(graph,ord(i[0])-97,ord(i[3])-97,set())
                if k:
                    return False
        return True
"""
#Attempt1 - Saw that this problem is a Union Find problem, so tried to use
#union find as in handbook. but couldn't work because 1 element can have
#friendship with many.
def find(uf,a):
    while(uf[a]!=a):
        a=uf[a]
    return a
    
    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations.sort(key=lambda x:x[1],reverse=True)
        ub=[i for i in range(26)]
        for i in equations:
            a,b=ord(i[0])-97,ord(i[3])-97
            if i[1]=='=':
                a,b=min(a,b),max(a,b)
                ub[b]=a
            else:
                if find(ub,a)==find(ub,b):
                        return False
        return True
                
            
"""
                
                
                
            
