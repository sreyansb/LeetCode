#attempt1:
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares_possible = []
        curno = 1
        while(curno*curno<=n):
            squares_possible.append(curno*curno)
            curno += 1
        squares_possible.append(n*n+1)#for a sentinel
        #if n==1, we will get n*n==1 and hence the sentinel is not good enough
        #therefore we use n*n+1

        #both alice and bob play optimally and person_wins shows if the person
        #can win only if the other person can't win
        @lru_cache(None)
        def person_wins(cur_val):
            if cur_val == 0:
                return False
            ans = False
            index = 0
            while(squares_possible[index]<=cur_val and not(ans)):
                ans = not(person_wins(cur_val - squares_possible[index]))
                index += 1
            return ans
        
        return person_wins(n)
    
        
