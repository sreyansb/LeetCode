#attempt2:Just made a change wherein I captured the number of subsequences with
#a difference instead of just appending each new occurenece to a list for the
# difference
from typing import *
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        print(n)
        liofdi=[{} for i in range(n)]
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]-nums[j] not in liofdi[i]:
                    liofdi[i][nums[i]-nums[j]]={}
                try:
                    for k in liofdi[j][nums[i]-nums[j]]:
                        if k+1 not in liofdi[i][nums[i]-nums[j]]:
                            liofdi[i][nums[i]-nums[j]][k+1]=0
                        liofdi[i][nums[i]-nums[j]][k+1]+=liofdi[j][nums[i]-nums[j]][k]
                except:
                    pass
                finally:
                    if 2 not in liofdi[i][nums[i]-nums[j]]:
                        liofdi[i][nums[i]-nums[j]][2]=0
                    liofdi[i][nums[i]-nums[j]][2]+=1
            for diff in liofdi[i]:
                for leng in liofdi[i][diff]:
                    deng=liofdi[i][diff][leng]
                    ans+=deng if leng>2 else 0
        return ans

#attempt1: TLE: 
# Idea: for every find index(starting from back) find each subsequence having
# a difference k at every index i
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        print(n)
        liofdi=[{} for i in range(n)]
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]-nums[j] not in liofdi[i]:
                    liofdi[i][nums[i]-nums[j]]=[]
                try:
                    for k in liofdi[j][nums[i]-nums[j]]:
                        liofdi[i][nums[i]-nums[j]].append(1+k)
                except:
                    pass
                finally:
                    liofdi[i][nums[i]-nums[j]].append(2)
            for diff in liofdi[i]:
                for leng in liofdi[i][diff]:
                    ans+=1 if leng>2 else 0
        return ans
'''