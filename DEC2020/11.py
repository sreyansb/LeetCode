#attempt1: nums could be empty
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if not(n):
            return 0
        index=1
        ele=nums[0]
        counts=1
        deleted=0
        arr=nums.copy()
        while(index<n):
            if arr[index]==ele:
                if counts==1:
                    counts+=1
                else:
                    nums.pop(index-deleted)
                    deleted+=1
            else:
                ele=arr[index]
                counts=1
            index+=1
        return len(nums)
        
