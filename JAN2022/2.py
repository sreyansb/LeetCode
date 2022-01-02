#attempt4: ans with arr[30] was done at the same place as arr[0]
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for i in range(60)]
        for i in time:
            arr[i%60] += 1
        
        ans = ((arr[0]*(arr[0]-1))>>1) + ((arr[30]*(arr[30]-1))>>1)
        for i in range(1,30):
            ans += arr[i]*arr[60-i]
        return ans

#attempt3: 282ms:replaced //2 by >>1
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for i in range(60)]
        for i in time:
            arr[i%60] += 1
        ans = (arr[0]*(arr[0]-1))>>1
        for i in range(1,30):
            ans += arr[i]*arr[60-i]
        ans += (arr[30]*(arr[30]-1))>>1
        return ans

#attempt2: 384ms
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for i in range(60)]
        for i in time:
            arr[i%60] += 1
        ans = (arr[0]*(arr[0]-1))//2
        for i in range(1,30):
            ans += arr[i]*arr[60-i]
        ans += (arr[30]*(arr[30]-1))//2
        return ans

#attempt1: WA because arr[0] should also have nC2 thing
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for i in range(60)]
        for i in time:
            arr[i%60] += 1
        ans = arr[0]
        for i in range(1,30):
            ans += arr[i]*arr[60-i]
        ans += (arr[30]*(arr[30]-1))//2
        return ans
'''
