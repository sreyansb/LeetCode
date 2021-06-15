#attempt3: DFS with pruning and sorting in decreasing order because pruning is completed
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        s=sum(matchsticks)
        reqd=s//4
        if s%4!=0:
            return False
        matchsticks.sort(reverse=True)
        @lru_cache(None)
        def check(index,s1,s2,s3,s4):
            if index>=n:
                return s1==s2==s3==s4
            if s1>reqd or s2>reqd or s3>reqd or s4>reqd:
                return False
            return check(index+1,s1+matchsticks[index],s2,s3,s4) or check(index+1,s1,s2+matchsticks[index],s3,s4) or check(index+1,s1,s2,s3+matchsticks[index],s4) or check(index+1,s1,s2,s3,s4+matchsticks[index])
        return check(0,0,0,0,0)

#attempt2: TLE DFS with just pruning
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        s=sum(matchsticks)
        reqd=s//4
        if s%4!=0:
            return False
        def check(index,s1,s2,s3,s4):
            if index>=n:
                return s1==s2==s3==s4
            if s1>reqd or s2>reqd or s3>reqd or s4>reqd:
                return False
            return check(index+1,s1+matchsticks[index],s2,s3,s4) or check(index+1,s1,s2+matchsticks[index],s3,s4) or check(index+1,s1,s2,s3+matchsticks[index],s4) or check(index+1,s1,s2,s3,s4+matchsticks[index])
        return check(0,0,0,0,0)
'''

#attempt1:TLE
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        s=sum(matchsticks)
        if s%4!=0:
            return False
        def check(index,s1,s2,s3,s4):
            if index>=n:
                return s1==s2==s3==s4
            return check(index+1,s1+matchsticks[index],s2,s3,s4) or check(index+1,s1,s2+matchsticks[index],s3,s4) or check(index+1,s1,s2,s3+matchsticks[index],s4) or check(index+1,s1,s2,s3,s4+matchsticks[index])
        return check(0,0,0,0,0)
'''