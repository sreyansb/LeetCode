#attempt4: AC added a check to see if the sum of the array %4 == 0
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        needed_sum = sum(matchsticks)
        if needed_sum % 4 != 0:
            return False
        needed_sum //= 4
        
        @lru_cache(None)
        def findsol(index,part1=needed_sum,part2=needed_sum,part3=needed_sum,part4=needed_sum):
            if index >= n:
                return part1==part2==part3==part4==0
            if part1<0 or part2<0 or part3<0 or part4<0:
                return False
            return findsol(index+1,part1-matchsticks[index],part2,part3,part4) or findsol(index+1,part1,part2-matchsticks[index],part3,part4) or findsol(index+1,part1,part2,part3-matchsticks[index],part4) or findsol(index+1,part1,part2,part3,part4-matchsticks[index])
        
        return findsol(0)
        

#attempt3:TLE : changed the way the function works to make each part go down to
#zero but doesn't help
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        needed_sum = sum(matchsticks)//4
        
        @lru_cache(None)
        def findsol(index,part1=needed_sum,part2=needed_sum,part3=needed_sum,part4=needed_sum):
            if index >= n:
                return part1==part2==part3==part4==0
            if part1<0 or part2<0 or part3<0 or part4<0:
                return False
            return findsol(index+1,part1-matchsticks[index],part2,part3,part4) or findsol(index+1,part1,part2-matchsticks[index],part3,part4) or findsol(index+1,part1,part2,part3-matchsticks[index],part4) or findsol(index+1,part1,part2,part3,part4-matchsticks[index])
        
        return findsol(0)
        
'''

#attempt2: TLE even with lru_cache
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        @lru_cache(None)
        def findsol(index,part1,part2,part3,part4):
            if index >= n:
                return part1==part2==part3==part4
            return findsol(index+1,part1+matchsticks[index],part2,part3,part4) or findsol(index+1,part1,part2+matchsticks[index],part3,part4) or findsol(index+1,part1,part2,part3+matchsticks[index],part4) or findsol(index+1,part1,part2,part3,part4+matchsticks[index])
        return findsol(0,0,0,0,0)
'''

#attempt1: TLE forgot lru_cache
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        def findsol(index,part1,part2,part3,part4):
            if index >= n:
                return part1==part2==part3==part4
            return findsol(index+1,part1+matchsticks[index],part2,part3,part4) or findsol(index+1,part1,part2+matchsticks[index],part3,part4) or findsol(index+1,part1,part2,part3+matchsticks[index],part4) or findsol(index+1,part1,part2,part3,part4+matchsticks[index])
        return findsol(0,0,0,0,0)
'''
