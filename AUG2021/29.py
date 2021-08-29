#attempt1:TOOK HELP
#1st idea : for every x from 1 to n: find if x can be formed using the given array
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        leng=len(nums)
        count=0
        cursum=1
        index=0
        while(cursum<=n):
            if index<leng and cursum>=nums[index]:
                cursum+=nums[index]
                index+=1
            else:
                cursum*=2
                count+=1
        return count