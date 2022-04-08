#attempt1: they want kth largest
from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_index = k-1
        self.nums = SortedList(nums,key=lambda x:-x)

    def add(self, val: int) -> int:
        self.nums.add(val)
        return self.nums[self.k_index]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
