#attempt1:
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final=[[]]
        for i in nums:
            newarr=[]
            for j in final:
                if j+[i] not in final:
                    newarr.append(j+[i])
            final=final+newarr
        return final