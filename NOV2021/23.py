#attempt unknown: COPIED the entire thing
#STILL DONT KNOW HOW TO FIND THE ANSWER
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        n=len(A)
        maxi=max(A)
        factors=[i for i in range(maxi+1)]
        
        def find(a):
            while(factors[a]!=a):
                factors[a]=factors[factors[a]]
                a=factors[a]
            return a
            
        def union(a,b):
            if factors[a]==factors[b]:
                return
            parenta=find(a)
            parentb=find(b)
            factors[parenta]=parentb
            
        for x in A:
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    union(x,i)
                    union(x,x//i)
        count={}
        for x in A:
            a=find(x)
            if a not in count:
                count[a]=0
            count[a]+=1
        return max(count.values())

