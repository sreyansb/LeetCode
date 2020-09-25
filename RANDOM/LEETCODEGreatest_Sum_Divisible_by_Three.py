#attempt2: We need to use DP -> saw hint



#Attempt1:  WA might be that our answer is wrong because dp[1] might be larger than dp[2] and so on
"""
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        di={0:[],1:[],2:[]}
        for i in nums:
            di[i%3].append(i)
        if di[0]:
            maxsum=sum(di[0])
        else:
            maxsum=0
        l=min(len(di[1]),len(di[2]))
        di[1].sort(reverse=True)
        di[2].sort(reverse=True)
        for j in range(l):
            maxsum+=di[1][j]+di[2][j]
        print(sum(di[1][l::3]),di[2][l::3])
        maxsum+=sum(di[1][l::3])
        maxsum+=sum(di[2][l::3])
        return maxsum
"""
