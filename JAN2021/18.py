#attempt2:- attempt1:WA-cant use abs(k-i) because k should be the larger number in the difference
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        di={}
        number=0
        for i in nums:
            if k-i in di:
                number+=1
                di[k-i]-=1
                if di[k-i]==0:
                    del di[k-i]
            else:
                if i not in di:
                    di[i]=0
                di[i]+=1
        return number
        
