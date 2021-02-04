#attempt1: TOOK HELP. It is simple, dont be afraid of subsequences
#order doesn't matter because it just maximum and minimum, dictionary with
#counts helps.The relative order would still be conserved as the array can have
#only x and (x-1 or x+1 and not both)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        di={}
        maxi=0
        for i in nums:
            if i not in di:
                di[i]=0
            di[i]+=1
        for n in set(nums):
            m=0
            if n+1 in di:
                m=di[n+1]
            if n-1 in di:
                m=max(m,di[n-1])
            maxi=max(maxi,m+di[n]) if m else maxi#very important condition
        return maxi
