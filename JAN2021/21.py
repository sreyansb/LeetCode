#attempt2: Took Help: We can have k windows and use heap approach to remove elements
#which are left to the minimum element
from heapq import heappush,heappop,heapify
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return [min(nums)]
        if k==len(nums):
            return nums
        ans=[]
        '''
        def findmin(arr,kval):
            #we need atleast kval-1 number of elements in the leftover array
            if kval==0:
                return
            mini=min(arr[:len(arr)-kval+1])
            ind=arr.index(mini)
            ans.append(mini)
            findmin(arr[ind+1:],kval-1)
        findmin(nums,k)
        '''
        heap=[(n,i) for i,n in enumerate(nums[:-k+1])]
        heapify(heap)
        ind=len(nums)-k+1
        for i in range(k):
            ele,index=heappop(heap)
            ans.append(ele)
            while(heap and heap[0][1]<index):
                heappop(heap)
            if i!=k-1:
                heappush(heap,(nums[ind+i],ind+i))
        return ans

#attempt1:TLE
'''
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return [min(nums)]
        if k==len(nums):
            return nums
        ans=[]
        def findmin(arr,kval):
            #we need atleast kval-1 number of elements in the leftover array
            if kval==0:
                return
            mini=min(arr[:len(arr)-kval+1])
            ind=arr.index(mini)
            ans.append(mini)
            findmin(arr[ind+1:],kval-1)
        findmin(nums,k)
        return ans
'''
