#attempt1:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        while(candidates and candidates[-1]>target):
            candidates.pop()
        ans = set()
        n = len(candidates)
        def create(curvis,cursum):

            if cursum == target:
                ans.add(tuple(sorted(curvis)))
                return
            
            for ele in candidates:
                if ele+cursum<=target:
                    create(curvis+[ele],ele+cursum)
        create([],0)
        return [list(i) for i in ans]
