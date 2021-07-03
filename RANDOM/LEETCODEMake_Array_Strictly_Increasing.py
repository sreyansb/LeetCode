#attempt2:TOOK HELP- > AC
'''
from bisect import bisect_right
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2=list(set(arr2))
        arr2.sort()
        n=len(arr1)
        m=len(arr2)
        @lru_cache(None)
        def recurse(index,parent):
            if index>=n:
                return 0
            ans=float('inf')
            if arr1[index]>parent:
                ans=min(ans,recurse(index+1,arr1[index]))
            i=bisect_right(arr2,parent)
            if i<m:
                ans=min(ans,1+recurse(index+1,arr2[i]))
            return ans
        ans=recurse(0,-1)
        return ans if ans!=float('inf') else -1
'''

#attempt1: TOOK HELP -> we need to maintain dp. For an index in arr1, we first need to see if the element there is greater than its parent i.e. previous
#Even if we have a valid position we will still try replacing it from arr2 based on binary search of the parent(bisect_right)
'''
from bisect import bisect_right
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2=list(set(arr2))
        arr2.sort()
        n=len(arr1)
        m=len(arr2)
        @lru_cache(None)
        def recurse(index,parent):
            if index>=n:
                return 0
            ans=float('inf')
            if arr1[index]>parent:
                ans=min(ans,recurse(index+1,arr1[index]))
            i=bisect_right(arr2,arr1[index])
            if i<m:
                ans=min(ans,1+recurse(index+1,arr2[i]))
            return ans
        ans=recurse(0,-1)
        return ans if ans!=float('inf') else -1
'''