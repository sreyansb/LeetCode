#attempt1:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n==0:
            return []
        ans = []
        ans.append([nums[0],nums[0]])
        for i in nums[1:]:
            if i == ans[-1][-1]+1 :
                ans[-1][-1] += 1
            else:
                ans.append([i,i])
        ans = [str(i[0])+"->"+str(i[1]) if i[0]!=i[1] else str(i[0]) for i in ans]
        return ans
        
                
                
        
