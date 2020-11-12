#attempt1 and 2-> 30% Took help
class Solution:
    def permuteUnique(self, a: List[int]) -> List[List[int]]:
        #my plan is to generate all the elements of the power set and navigate through it to find length of each
        #i found powerset which was wrong
        ans=set()      
        def permute(start,end):
            if start==end:
                k=a.copy()
                ans.add(tuple(k))
                return
            for i in range(start,end+1):
                a[start],a[i]=a[i],a[start]
                permute(start+1,end)
                a[start],a[i]=a[i],a[start]
        permute(0,len(a)-1)
        ans=list(ans)
        for i in range(len(ans)):
            ans[i]=list(ans[i])
        return ans
                
            
            
                
                
                
                
                
                
        
