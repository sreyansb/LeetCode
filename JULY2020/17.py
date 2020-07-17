#MAKING into buckets and solving
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        maxfreq=0
        for i in nums:
            if i not in di:
                di[i]=0
            di[i]+=1
            maxfreq=max(maxfreq,di[i])
        frequency=[[] for i in range(maxfreq+1)]
        for i in di:
            frequency[di[i]].append(i)
        sol=[]
        for j in frequency[::-1]:
            sol+=j[:min(k,len(j))]
            k-=len(j[:min(k,len(j))])
            if k==0:
                break
        return sol
            
            
        
"""
#FASTER SOLUTION
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        for i in nums:
            if i not in di:
                di[i]=0
            di[i]+=1
        j=sorted(di,key=lambda x:di[x],reverse=True)
        return j[:k]
        
"""
