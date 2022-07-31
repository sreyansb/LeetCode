#attempt1:
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.segmenttree = [0]*(4*n)
        self.nums = nums.copy()
        self.leng = len(self.nums)-1
        
        def buildtree(left_nums,right_nums,segment_index):
            if left_nums > right_nums:
                return 0
            if left_nums == right_nums:
                self.segmenttree[segment_index] = nums[left_nums]
                return self.segmenttree[segment_index]
            mid = (left_nums+right_nums)//2
            self.segmenttree[segment_index] = buildtree(left_nums,mid,2*segment_index+1) + buildtree(mid+1,right_nums,2*segment_index+2)
            return self.segmenttree[segment_index]
        buildtree(0,self.leng,0)
        print(self.segmenttree)
        
    def update(self, index: int, val: int) -> None:
        diff_to_be_added = val - self.nums[index]
        self.nums[index] = val
        def updatesegment(left_nums,right_nums,segment_index,diff_to_be_added):
            if left_nums > right_nums or not(left_nums<=index<=right_nums):
                return
            if left_nums == right_nums:
                self.segmenttree[segment_index] += diff_to_be_added
                return
            self.segmenttree[segment_index] += diff_to_be_added
            mid = (left_nums+right_nums)//2
            updatesegment(left_nums,mid,2*segment_index+1,diff_to_be_added)
            updatesegment(mid+1,right_nums,2*segment_index+2,diff_to_be_added)
        updatesegment(0,self.leng,0,diff_to_be_added)
            
    def sumRange(self, left: int, right: int) -> int:
        
        def sumsegment(left_required,right_required,left_nums,right_nums,segment_index):
            if left_nums>right_nums:
                return 0
            if right_required < left_nums or left_required>right_nums:
                return 0
            if (left_required<=left_nums) and (right_nums<=right_required):
                return self.segmenttree[segment_index]
            mid = (left_nums+right_nums)//2
            return sumsegment(left_required,right_required,left_nums,mid,2*segment_index+1) + sumsegment(left_required,right_required,mid+1,right_nums,2*segment_index+2)
        return sumsegment(left,right,0,self.leng,0)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
