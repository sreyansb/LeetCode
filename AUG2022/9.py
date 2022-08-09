#attempt1:ToOK HELP
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arrset = set(arr)
        divisible_by = {}
        for i in range(len(arr)):
            divisible_by[arr[i]] = []
            for j in range(len(arr)):
                if arr[i]%arr[j] == 0:
                    if arr[i]//arr[j] in arrset:
                        divisible_by[arr[i]].append((arr[j],arr[i]//arr[j]))
        print(divisible_by)
        ans = 0
        answers = {}
        for i in sorted(divisible_by.keys()):
            anshere = 1
            for a,b in divisible_by[i]:
                anshere += (answers[a]*answers[b])
            ans += anshere
            answers[i] = anshere
        return ans%(1000000007)
            
            
        
        
        
