#BUCKET_SORT problem - had to take help
#in each bucket - the max difference that can be there is t.
#we sort into buckets based on nums[i] value.
#bcoz of (%(t+1)) max-diff values can be t.
#We only need to store the most recent value of a bucket.
#the differences might be in same bucket or just +,- 1 buckets.
#check the values and solve.
#ATTEMPT-3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n=len(nums)
        if n==0 or k<=0 or t<0:
            return False
        index=0
        width=t+1 #we need t+1 as t = 0=>error
        di={}
        while(index<n):
            position=nums[index]//width
            if position in di:
                return True
            if position-1 in di and abs(di[position-1]-nums[index])<=t:
                return True
            if position+1 in di and abs(di[position+1]-nums[index])<=t:
                return True
            di[position]=nums[index]
            if index>=k:
                del di[nums[index-k]//width]
            index+=1
        return False

#ATTEMPT-2
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n=len(nums)
        for i in range(n):
            l=nums[i+1:min(n,i+k+1)]
            l.sort()
            for j in l:
                if abs(nums[i]-j)<=t:
                    return True
        return False
"""

#ATTEMPT-1
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n=len(nums)
        for i in range(n):
            l=nums[i+1:min(n,i+k+1)]
            l.sort()
            for j in l:
                if abs(nums[i]-j)<=t:
                    return True
        return False
"""


