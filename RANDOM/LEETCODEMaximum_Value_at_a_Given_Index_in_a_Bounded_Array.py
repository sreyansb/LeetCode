#attempt3: 
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n==1:
            return maxSum
        start=1
        end=maxSum
        ans=-1
        left=index
        right=n-1-index
        
        #print(left,right)
        while(start<=end):
            mid=(start+end)//2
            v1=((mid-1)*mid)//2
            if mid-1<=index:
                v1+=index-mid+1
            else:
                v1-=((mid-index-1)*(mid-index))//2
            v2=((mid-1)*mid)//2
            if mid-1<=right:
                v2+=right-mid+1
            else:
                v2-=((mid-right-1)*(mid-right))//2
            if mid+v1+v2>maxSum:
                end=mid-1
            else:
                ans=mid
                start=mid+1        
        return ans

#attempt2: WA Completely overhauled the method. WA because in the sum for right part didnt change value to right
'''class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n==1:
            return maxSum
        start=1
        end=maxSum
        ans=-1
        right=n-1-index
        while(start<=end):
            mid=(start+end)//2
            v1=((mid-1)*mid)//2
            if mid-1<=index:
                v1+=index-mid+1
            else:
                v1-=((mid-index-1)*(mid-index))//2
            v2=((mid-1)*mid)//2
            if mid-1<=right:
                v2+=index-mid+1
            else:
                v2-=((mid-right-1)*(mid-right))//2
            if mid+v1+v2>maxSum:
                end=mid-1
            else:
                ans=mid
                start=mid+1
            #print(mid,v1,v2)
        
        return ans'''

#attempt1: WA because the bounding was not right
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n==1:
            return maxSum
        start=1
        end=maxSum
        ans=-1
        left=index
        right=n-1-index
        left=(left*(left+1))//2
        right=(right*(right+1))//2
        while(start<=end):
            mid=(start+end)//2
            if n*mid-(left+right)>maxSum:
                end=mid-1
            else:
                ans=mid
                start=mid+1
        return ans
        
'''