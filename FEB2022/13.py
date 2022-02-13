#attempt1:Kya hai bhai
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = [[]]
        for i in nums:
            new = []
            for j in final:
                new.append(j+[i])
            final.extend(new)
        return final
        
