#attempt4: 3 attempts and some help later
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        shareBoundary = [set() for i in range(n)]
        for firstIndex in range(n):
            for secondIndex in range(firstIndex+1,n):
                if stones[firstIndex][0] == stones[secondIndex][0] or stones[firstIndex][1] == stones[secondIndex][1]:
                    shareBoundary[firstIndex].add(secondIndex)
                    shareBoundary[secondIndex].add(firstIndex)
        
        maxAns = 0
        allVisited = set()
        def connectedComponents(curIndex,currentVisited = set()):
            
            currentVisited.add(curIndex)
            for nextVertex in shareBoundary[curIndex]:
                if nextVertex not in currentVisited:
                    connectedComponents(nextVertex,currentVisited)
            return 0
        
        for index in range(n):
            if index not in allVisited:
                newVisited = set()
                connectedComponents(index, newVisited)
                #print(index, newVisited)
                allVisited = allVisited | newVisited
                maxAns += len(newVisited)-1
        
        return maxAns
