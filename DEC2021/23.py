#attempt1: Toposort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inedges = {}
        for i in range(numCourses):
            inedges[i] = set()
        outedges = {}
        for c2,c1 in prerequisites:
            if c1 not in outedges:
                outedges[c1] = set()
            outedges[c1].add(c2)
            inedges[c2].add(c1)
        #print(inedges,outedges)
        ordering = []
        while(inedges):
            curvertex = -1
            for i in inedges:
                if not(inedges[i]):
                    curvertex = i
                    break
            if curvertex == -1:
                return []
            ordering.append(curvertex)
            del inedges[curvertex]
            if curvertex in outedges:
                for affectedvertex in outedges[curvertex]:
                    inedges[affectedvertex].remove(curvertex)
        return ordering
                
            
        
        
