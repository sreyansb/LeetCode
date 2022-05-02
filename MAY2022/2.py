#attempt2 : AC
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenindex = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                temp = nums[evenindex]
                if (temp%2 == 0):
                    nums[evenindex],nums[i] = nums[i],nums[evenindex]
                else:
                    while(evenindex<i and nums[evenindex]%2 == 0):
                        evenindex += 1
                    nums[evenindex],nums[i] = nums[i],nums[evenindex]
                evenindex += 1
        return nums
                
#attempt1: WA : because evenindex has to be increased even in if condition
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenindex = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                temp = nums[evenindex]
                if (temp%2 == 0):
                    nums[evenindex],nums[i] = nums[i],nums[evenindex]
                else:
                    while(evenindex<i and nums[evenindex]%2 == 0):
                        evenindex += 1
                    nums[evenindex],nums[i] = nums[i],nums[evenindex]
                    evenindex += 1
        return nums
                
            
        
'''
