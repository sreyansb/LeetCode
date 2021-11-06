#attempt3: TOOK HINT: a and b are different and hence a^b would have atleast one
#set bit and hence we need to find that. XOR ans1 with array elements if mask and i are 1
# and get the first element. Then using the xor value of the array we get the second
#element
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        mask = 1
        while(1):
            if mask&xor:
                break
            mask <<= 1
        ans1,ans2 = 0,-1
        for i in nums:
            if mask&i:
                ans1 ^= i
        for i in nums:
            if ans1^i == xor:
                ans2 = i
        return [ans1,ans2]

#attempt2: WA- mask can be affected by other values also.
#So we would have to XOR it to find ans1
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        mask = 1
        while(1):
            if mask&xor:
                break
            mask <<= 1
        
        ans1,ans2 = -1,-1
        for i in nums:
            if mask&i:
                ans1 = i
                break
        for i in nums:
            if ans1^i == xor:
                ans2 = i
        return [ans1,ans2]
'''
#attempt1: AC : 56ms and 16.4MB
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        di = {}
        for i in nums:
            if i in di:
                del di[i]
            else:
                di[i] = 1
        return di.keys()
                
        
        
'''
