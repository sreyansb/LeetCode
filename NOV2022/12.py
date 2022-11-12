#attempt1:
from heapq import heappush
class MedianFinder:

    def __init__(self):
        self.lowerHalf = []
        self.upperHalf = []
        self.lowerLen = 0
        self.upperLen = 0        

    def addNum(self, num: int) -> None:
        toBeAddedTo,valueToBeAdded = None, num
        if self.lowerLen and num <= -self.lowerHalf[0]:
            valueToBeAdded *= -1
            toBeAddedTo = "lower"
        else:
            toBeAddedTo = "upper"

        if self.lowerLen == self.upperLen:
            if toBeAddedTo == "lower":
                heappush(self.lowerHalf,valueToBeAdded)
                self.lowerLen += 1
            else:
                heappush(self.upperHalf,valueToBeAdded)
                self.upperLen += 1
        elif self.lowerLen < self.upperLen:
            if toBeAddedTo == "upper":
                heappush(self.upperHalf,num)
                valueToBeAdded = -heappop(self.upperHalf)
            heappush(self.lowerHalf,valueToBeAdded)
            self.lowerLen += 1
        else:
            if toBeAddedTo == "lower":
                heappush(self.lowerHalf,-num)
                valueToBeAdded = -heappop(self.lowerHalf)
            heappush(self.upperHalf,valueToBeAdded)
            self.upperLen += 1   
        #print(self.lowerHalf,self.upperHalf,self.lowerLen,self.upperLen)         

    def findMedian(self) -> float:
        if self.lowerLen == self.upperLen:
            return (-self.lowerHalf[0] + self.upperHalf[0])/2
        if self.lowerLen < self.upperLen:
            return self.upperHalf[0]
        return -self.lowerHalf[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
