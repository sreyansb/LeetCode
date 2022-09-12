#attempt2:
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start = 0
        end = len(tokens)-1
        currentScore = 0
        maxScore = 0
        currentPower = power
        while(start <= end):
            if currentPower >= tokens[start]:
                currentPower -= tokens[start]
                currentScore += 1
                maxScore = max(maxScore,currentScore)
                start += 1
            else:
                currentPower += tokens[end]
                currentScore -= 1
                end -= 1
                if currentScore < 0:
                    break
        return maxScore
                
            

#attempt1: WA because currentScore can't be < 0
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start = 0
        end = len(tokens)-1
        currentScore = 0
        maxScore = 0
        currentPower = power
        while(start <= end):
            if currentPower >= tokens[start]:
                currentPower -= tokens[start]
                currentScore += 1
                maxScore = max(maxScore,currentScore)
                start += 1
            else:
                currentPower += tokens[end]
                currentScore -= 1
                end -= 1
        return maxScore
'''
