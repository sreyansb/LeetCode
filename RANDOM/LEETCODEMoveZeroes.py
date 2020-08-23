#attempt 2->Satisfies inplace and stable sort
#it is quite a problem
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index=0
        while(index<len(nums)):
            if nums[index]:
                break
            index+=1
        lin=0
        while(lin<len(nums)):
            if nums[lin]==0 and index>lin and index<len(nums):
                nums[index],nums[lin]=nums[lin],nums[index]
                while(index<len(nums)):
                    if nums[index]:
                        break
                    index+=1
            elif nums[lin]:
                index=lin+1
                while(index<len(nums)):
                    if nums[index]:
                        break
                    index+=1
            lin+=1
        
                
                
        
            
        
        
        
