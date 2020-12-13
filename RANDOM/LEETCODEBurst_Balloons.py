#attempt1 :Same as december 13,2020
#ONE OF THE BEST PROBLEMS TO SOLVE
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+[i for i in nums if i>0]+[1]
        dpt={}
        def dp(lindex,rindex):
            if lindex+1==rindex:
                return 0
            if (lindex,rindex) not in dpt:
                dpt[(lindex,rindex)]=max([dp(lindex,i)+nums[lindex]*nums[i]*nums[rindex]+dp(i,rindex) for i in range(lindex+1,rindex)])
            return dpt[(lindex,rindex)]
        return dp(0,len(nums)-1)
            
        
