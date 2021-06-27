#attempt2: Prefix and sufix sum
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1:
            return 1
        right=[1 for i in range(n)]
        left=[1 for i in range(n)]
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        ans=[max(right[i],left[i]) for i in range(n)]
        return sum(ans)


#attempt1:WA for [29,51,87,87,72,12]
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1:
            return [1]
        ans=[1 for i in range(n)]
        if ratings[0]>ratings[1]:
            ans[0]+=1
        if ratings[-1]>ratings[-2]:
            ans[-1]+=1
        for i in range(1,n-1):
            if ratings[i-1]<ratings[i] or ratings[i]>ratings[i+1]:
                ans[i]=max(ans[i-1],ans[i+1])+1
        return sum(ans)
'''