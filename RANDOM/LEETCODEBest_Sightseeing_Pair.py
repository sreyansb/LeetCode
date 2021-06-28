#attempt3: For an index: Add the element at that index according to rules to prev_max
#For an index: prev_max is sort of hidden and all we need to store is max(prev_max,A[index]+index)

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        prev_max,ans=0,0
        for i in range(len(A)):
            ans=max(ans,prev_max+A[i]-i)
            prev_max=max(prev_max,A[i]+i)
        return ans

#attempt2: WA: took a max and tried to find the corresponding answer
#Attempt should be that A[index]+index matters
'''
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxie,index=-1,-1
        for i in range(len(A)):
            if maxie<A[i]:
                maxie=A[i]
                index=i
        ans=0
        for i in range(index-1,-1,-1):
            ans=max(ans,maxie+A[i]-index+i)
        for i in range(index+1,len(A)):
            ans=max(ans,maxie+A[i]+index-i)
        return ans
'''

#attempt1: WA Just took the most probable answers
'''
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        init = [A[0],A[1],0,1]
        index=1
        while(index<len(A)):
            if init[1]+A[index]-index+init[3]>init[0]+init[1]+init[2]-init[3] and index!=init[3]:
                init[0]=init[1]
                init[1]=A[index]
                init[2]=init[3]
                init[3]=index
            elif A[index]+init[0]+init[2]-index>init[0]+init[1]+init[2]-init[3] and index!=init[3]:
                init[1]=A[index]
                init[3]=index
            index+=1
        return init[0]+init[1]+init[2]-init[3]
'''