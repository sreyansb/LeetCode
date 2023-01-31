#attempt2:
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        zippedAgedScore = [(ages[i],scores[i]) for i in range(n)]
        zippedAgedScore.sort(key = lambda x:(x[0],x[1]))

        @lru_cache(None)
        def dfs(index):
            if index >= n:
                return 0
            curAge,curScore = zippedAgedScore[index]
            maxSeenHere = curScore
            for nextIndex in range(index+1,n):
                if zippedAgedScore[nextIndex][1] < curScore:
                    continue
                maxSeenHere = max(maxSeenHere, curScore + dfs(nextIndex))
            return maxSeenHere
        
        maxAns = max(scores)
        for index in range(n):
            maxAns = max(maxAns,dfs(index))

        return maxAns
                
#attempt1: WA because you might want to optimize the next index  you take
'''
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        zippedAgedScore = [(ages[i],scores[i]) for i in range(n)]
        zippedAgedScore.sort(key = lambda x:(x[0],x[1]))
        highestSeen = -float('inf')
        for index in range(n):
            age,score = zippedAgedScore[index]
            currentSum = 0
            for nextIndex in range(index,n):
                newAge,newScore = zippedAgedScore[nextIndex]
                if newScore < score:
                    continue
                currentSum += newScore
                highestSeen = max(highestSeen, currentSum)
                score = max(score, newScore)
            #print(index, currentSum)
        return highestSeen
                
                

'''
