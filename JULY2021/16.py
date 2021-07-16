#attempt1:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=set()
        n=len(nums)
        for a in range(n):
            for b in range(a+1,n):
                di={}
                for c in range(b+1,n):
                    if target-(nums[a]+nums[b]+nums[c]) in di:
                        for i in di[target-(nums[a]+nums[b]+nums[c])]:
                            ans.add(tuple(sorted(i+[nums[c]])))
                    if nums[c] not in di:
                        di[nums[c]]=[]
                    di[nums[c]].append([nums[a],nums[b],nums[c]])
        return [list(i) for i in ans]
                