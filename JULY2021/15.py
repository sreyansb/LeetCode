#attempt2: TOOK HELP: the main issue was the index part
#i.e. finding indices for s3 and if s1+s3>s2.
# So the main idea is to sort the array and keeping the stuff
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        for is3 in range(n-1,1,-1):
            is1=0
            is2=is3-1
            s3=nums[is3]
            while(is1<is2):
                s2=nums[is2]
                s1=nums[is1]
                if s1+s2>s3:
                    count+=is2-is1
                    is2-=1
                else:
                    is1+=1
        return count

#attempt1: TLE O(n3) is the solutiion
#idea was to find all possible sums between two sides and then do a 
#bisect right for each element on the sums so that we could get
#all sides with sums>current side
'''
from bisect import bisect_right
from sortedcontainers import SortedList
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        di={}
        sumarray=SortedList([])
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] not in di:
                    di[nums[i]+nums[j]]=[]
                    sumarray.add(nums[i]+nums[j])
                di[nums[i]+nums[j]].append([i,j])
        lsa=len(sumarray)
        #print(sumarray,di)
        count=set()
        for is3 in range(n):
            s3=nums[is3]
            pos=sumarray.bisect_right(s3)
            for biggersumindex in range(pos,lsa):
                for is1,is2 in di[sumarray[biggersumindex]]:
                    if is1!=is3 and is3!=is2:
                        s1=nums[is1] 
                        s2=nums[is2]
                        if s1+s3>s2 and s3+s2>s1:
                            count.add(tuple(sorted((is1,is2,is3))))
        return len(count)
'''