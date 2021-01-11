#attempt2: Took help - 98%- 2 pointer approach->has to be from back and not front
#so that we can still hold the values and none of them are lost
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            return
        p1,p2=m-1,n-1
        for i in range(m+n-1,-1,-1):
            if p2<0 or p1<0:
                break
            if nums1[p1]>nums2[p2]:
                nums1[i]=nums1[p1]
                p1-=1
            else:
                nums1[i]=nums2[p2]
                p2-=1
        while(p2>-1):
            nums1[i]=nums2[p2]
            p2-=1
            i-=1
        return

#attempt1: AC very slow
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
            return
        i=0
        while(i<m):
            if nums1[i]>nums2[0]:
                nums1[i],nums2[0]=nums2[0],nums1[i]
            i+=1
        nums2.sort()
        for i in range(n):
            nums1[i+m]=nums2[i]
        return
        
'''
