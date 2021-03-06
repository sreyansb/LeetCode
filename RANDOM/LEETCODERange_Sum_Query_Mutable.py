#attempt1: NEW LEARNING
#FENWICK TREE - Binary Indexed Tree
#using fenwick tree
#use the right most set bit of an index i i&-i for the problem
#logn for updates and sum queries because max number of bits in a number n = log n

class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.nums=[0]+nums
        self.n+=1
        self.fen=self.nums.copy()
        for i in range(1,self.n):
            j=i+((i&-i))
            if j<self.n:
                self.fen[j]+=self.fen[i]    
        #print(self.fen)

    def update(self, index: int, val: int) -> None:
        index+=1
        diff=val-self.nums[index]
        self.nums[index]=val
        while(index<self.n):
            self.fen[index]+=diff
            index=index+((index&-index))
        
    def sumRange(self, left: int, right: int) -> int:
        ansl=0
        while(left>0):
            ansl+=self.fen[left]
            left-=((left&-left))
        right+=1
        ansr=0
        while(right>0):
            ansr+=self.fen[right]
            right-=((right&-right))
        return ansr-ansl


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
