#attempt1:
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dpt={}
        dpt[0]=1
        def check(tar):
            if tar==0:
                return 1
            if tar in dpt:
                return dpt[tar]
            x=0
            for i in nums:
                if tar-i>=0:
                    x+=check(tar-i)#only check(tar-i) because there is only one
                    #way of selecting i waala coin
            dpt[tar]=x
            return dpt[tar]
        check(target)
        #print(dpt)
        return dpt[target]
        
