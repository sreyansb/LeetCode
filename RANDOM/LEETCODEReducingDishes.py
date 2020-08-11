#very fast
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maxi=0
        givensum=0
        satisfaction.sort(reverse=True)
        for i in satisfaction:
              if givensum+i>0:
                    givensum+=i
                    maxi+=givensum
        return maxi
            
        

#very slow -> lot of space and very slow.
#it was a pure DP answer but couldn't be fast.
"""
def helper(index,satisfaction,time,di):
    if index>=len(satisfaction):
        return 0
    if di[index][time]!=-1:
        return di[index][time]
    di[index][time]=max(0,helper(index+1,satisfaction,time+1,di)+satisfaction[index]*time,helper(index+1,satisfaction,time,di))
    
    return di[index][time]
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maxi=0
        satisfaction.sort()
        time=1
        dp=[[-1 for i in range(510)] for j in range(510)]
        maxi=helper(0,satisfaction,time,dp)
        return maxi
"""         
        
