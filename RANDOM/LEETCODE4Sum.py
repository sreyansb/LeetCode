#attempt1:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=set()
        n=len(nums)
        di={}
        for i in range(n-3):
            for j in range(i+1,n-2):
                for k in range(j+1,n):
                    if target-(nums[k]) in di:
                        for z in di[target-nums[k]]:
                            if k not in z:
                                y=[nums[a] for a in z]
                                ans.add(tuple(sorted(y+[nums[k]])))
                            #print(z,ans)
                    if nums[i]+nums[j]+nums[k] not in di:
                        di[nums[i]+nums[j]+nums[k]]=[]
                    di[nums[i]+nums[j]+nums[k]].append([i,j,k])
        #print(di[11])
        return [list(i) for i in ans]
