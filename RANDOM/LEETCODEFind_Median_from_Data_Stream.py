#A median (the middle element of the stream)
#separates the smaller elements from the larger ones.
#So we maintain 2 heaps: minheap to keep larger elements
#maxheap to keep smaller elements 
#the reason being that the nearest elements to the mid will be the smallest
#among the largest elements and largest amongst the smallest elements.

#heapq implements maxheap

from heapq import heappush,heappop

class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        self.cur_med=0       
        
    def addNum(self, ele: int) -> None:
        if len(self.minheap)<len(self.maxheap):
            if ele>=self.cur_med:
                heappush(self.minheap,ele)
                self.cur_med=(self.minheap[0]-self.maxheap[0])/2
            else:
                elt=heappop(self.maxheap)
                heappush(self.maxheap,-ele)
                heappush(self.minheap,-elt)
                self.cur_med=(self.minheap[0]-self.maxheap[0])/2
        elif len(self.minheap)>len(self.maxheap):
            if ele>=self.cur_med:
                elt=heappop(self.minheap)
                heappush(self.maxheap,-elt)
                heappush(self.minheap,ele)
                self.cur_med=(self.minheap[0]-self.maxheap[0])/2
            else:
                heappush(self.maxheap,-ele)
                self.cur_med=(self.minheap[0]-self.maxheap[0])/2
        else:
            if ele>=self.cur_med:
                heappush(self.minheap,ele)
                self.cur_med=self.minheap[0]
            else:
                heappush(self.maxheap,-ele)
                self.cur_med=-self.maxheap[0]             

    def findMedian(self) -> float:
        return self.cur_med
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
