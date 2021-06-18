#attempt2: SEGMENT TREE
#attempt1: SEGMENT TREE
class NumArray:
    
    def __init__(self, nums: List[int]):
        n=len(nums)
        self.segmenttree=[0]*(4*n)
        self.array=nums.copy()
        self.n=n
        def fill(si,l,r):
            if l==r:
                self.segmenttree[si]=self.array[l]
                return self.segmenttree[si]
            mid=(l+r)//2
            self.segmenttree[si]=fill(2*si+1,l,mid)+fill(2*si+2,mid+1,r)
            return self.segmenttree[si]
        
        fill(0,0,n-1)
        
    def update(self, index: int, val: int) -> None:
        diff=val-self.array[index]
        self.array[index]=val
        def updatekaro(si,sl,sr,index,diff):
            if index<sl or index>sr:
                return
            self.segmenttree[si]+=diff
            if sl!=sr:
                mid=(sl+sr)//2
                updatekaro(2*si+1,sl,mid,index,diff)
                updatekaro(2*si+2,mid+1,sr,index,diff)
        updatekaro(0,0,self.n-1,index,diff)
        
    def sumRange(self, left: int, right: int) -> int:
        def sumkaro(si,sl,sr,l,r):
            if (l<=sl<=r) and (l<=sr<=r):
                return self.segmenttree[si]
            if sr<l or sl>r:
                return 0
            mid=(sl+sr)//2
            return sumkaro(2*si+1,sl,mid,l,r)+sumkaro(2*si+2,mid+1,sr,l,r)
        return sumkaro(0,0,self.n-1,left,right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

#attempt1: NEW LEARNING
#FENWICK TREE - Binary Indexed Tree
#using fenwick tree
#use the right most set bit of an index i i&-i for the problem
#logn for updates and sum queries because max number of bits in a number n = log n
'''
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
'''