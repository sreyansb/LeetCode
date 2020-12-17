#attempt1:60% and 60%- get the sum of first 2 and others also
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        di1={}
        di2={}
        for i in A:
            for j in B:
                if i+j not in di1:
                    di1[i+j]=0
                di1[i+j]+=1
        ans=0
        for i in C:
            for j in D:
                if -(i+j) in di1:
                    ans+=di1[-(i+j)]
        return ans
        
