#attempt2: 567ms
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        def my_rev(start,end):
            while(start<=end):
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        my_rev(n-k,n-1)
        my_rev(0,n-k-1)
        my_rev(0,n-1)
        #print(nums)
        #nums.reverse()

#attempt1: 384ms AC
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[n-k:] = nums[n-k:][::-1]
        #print(nums)
        nums[:n-k] = nums[:n-k][::-1]
        #print(nums)
        nums.reverse()
        
