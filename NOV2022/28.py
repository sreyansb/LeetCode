#attempt1:
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = {}
        for match in matches:
            winner, loser = match
            winners.add(winner)
            if loser not in losers:
                losers[loser] = 0
            losers[loser] += 1
        return [sorted(winners-set(losers.keys())), sorted([key for key in losers if losers[key] == 1])]
            
