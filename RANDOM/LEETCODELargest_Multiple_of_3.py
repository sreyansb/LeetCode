#attempt4: AC we remove the smallest element which is making the sum non divisible
#by 3
from heapq import heappush,heappop
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        heap1=[]
        heap2=[]
        ans=""
        for i in digits:
            if i%3==0:
                ans+=str(i)
            elif i%3==1:
                heappush(heap1,i)
            else:
                heappush(heap2,i)
        n=len(digits)
        if sum(digits)%3==1:
            if heap1:
                heappop(heap1)
            else:
                heappop(heap2)
                heappop(heap2)
        elif sum(digits)%3==2:
            if heap1:
                heappop(heap2)
            else:
                heappop(heap1)
                heappop(heap1)
            
        while(heap1 and heap2):
            ans+=str(heappop(heap1))+str(heappop(heap2))
        while(len(heap1)>2):
            ans+=str(heappop(heap1))+str(heappop(heap1))+str(heappop(heap1))
        while(len(heap2)>2):
            ans+=str(heappop(heap2))+str(heappop(heap2))+str(heappop(heap2))
        
        
        #print(ans)
        if set(ans)=={"0"}:
            return "0"
        return "".join(sorted(ans,reverse=True)).lstrip("0")

#attempt3: WA we cant just change the order of evaluation: 22111
'''
from heapq import heappush,heappop
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        heap0=[]
        heap1=[]
        heap2=[]
        for i in digits:
            if i%3==0:
                heappush(heap0,-i)
            elif i%3==1:
                heappush(heap1,-i)
            else:
                heappush(heap2,-i)
        ans=""
        n=len(digits)
        while(len(heap1)>2):
            ans+=str(-heappop(heap1))+str(-heappop(heap1))+str(-heappop(heap1))
        while(len(heap2)>2):
            ans+=str(-heappop(heap2))+str(-heappop(heap2))+str(-heappop(heap2))
        while(heap1 and heap2):
            ans+=str(-heappop(heap1))+str(-heappop(heap2))
        while(heap0):
            ans+=str(-heappop(heap0))
        
        
        #print(ans)
        if set(ans)=={"0"}:
            return "0"
        return "".join(sorted(ans,reverse=True)).lstrip("0")        
'''

#attempt2: WA because you can take 2 1s instead of 1 2
'''
from heapq import heappush,heappop
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        heap0=[]
        heap1=[]
        heap2=[]
        for i in digits:
            if i%3==0:
                heappush(heap0,-i)
            elif i%3==1:
                heappush(heap1,-i)
            else:
                heappush(heap2,-i)
        ans=""
        n=len(digits)
        while(heap0):
            ans+=str(-heappop(heap0))
        while(heap1 and heap2):
            ans+=str(-heappop(heap1))+str(-heappop(heap2))
        while(len(heap1)>2):
            ans+=str(-heappop(heap1))+str(-heappop(heap1))+str(-heappop(heap1))
        while(len(heap2)>2):
            ans+=str(-heappop(heap2))+str(-heappop(heap2))+str(-heappop(heap2))
        #print(ans)
        if set(ans)=={"0"}:
            return "0"
        return "".join(sorted(ans,reverse=True)).lstrip("0")
'''

#attempt1: TLE TIME TOH lagega hi
'''
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        n=len(digits)
        ans=[-float('inf')]
        if digits[-1]==0:
            ans=[0]
        digits.sort(reverse=True)
        @lru_cache(None)
        def recurse(index,pastsum,curnum):
            if index>=n:
                if curnum and pastsum%3==0:
                    ans[0]=max(ans[0],curnum)
                return
            recurse(index+1,pastsum+digits[index],curnum*10+(digits[index]))
            recurse(index+1,pastsum,curnum)
        recurse(0,0,0)
        return str(ans[0]) if ans[0]!=-float('inf') else ""
'''
