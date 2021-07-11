#attempt3: AC after adding median part
from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        self.lowers=[]
        self.uppers=[]
        self.ln=0
        self.up=0
        self.leng=0
        self.median=0
        
    def addNum(self, num: int) -> None:
        self.leng+=1
        if self.ln==self.up:
            if num<=self.median:
                heappush(self.lowers,-num)
                self.ln+=1
            else:
                heappush(self.uppers,num)
                self.up+=1
        elif self.ln<self.up:
            if num<=self.median:
                heappush(self.lowers,-num)
                self.ln+=1
            else:
                heappush(self.uppers,num)
                ele=heappop(self.uppers)
                heappush(self.lowers,-ele)
                self.ln+=1
        else:
            if num>self.median:
                heappush(self.uppers,num)
                self.up+=1
            else:
                heappush(self.lowers,-num)
                ele=heappop(self.lowers)
                heappush(self.uppers,-ele)
                self.up+=1
        if self.leng%2:
            if self.ln>self.up:
                self.median=-self.lowers[0]
            else:
                self.median=self.uppers[0]
        else:
            self.median=(self.uppers[0]-self.lowers[0])/2

    def findMedian(self) -> float:
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#attempt1&2: WA because like an idiot I didn't calculate median after every insertion
'''
from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        self.lowers=[]
        self.uppers=[]
        self.ln=0
        self.up=0
        self.leng=0
        self.median=0
        
    def addNum(self, num: int) -> None:
        self.leng+=1
        if self.ln==self.up:
            if num<=self.median:
                heappush(self.lowers,-num)
                self.ln+=1
            else:
                heappush(self.uppers,num)
                self.up+=1
        elif self.ln<self.up:
            if num<=self.median:
                heappush(self.lowers,-num)
                self.ln+=1
            else:
                heappush(self.uppers,num)
                ele=heappop(self.uppers)
                heappush(self.lowers,-ele)
                self.ln+=1
        else:
            if num>self.median:
                heappush(self.uppers,num)
                self.up+=1
            else:
                heappush(self.lowers,-num)
                ele=heappop(self.lowers)
                heappush(self.uppers,ele)
                self.up+=1

    def findMedian(self) -> float:
        if self.leng%2:
            if self.ln>self.up:
                return -self.lowers[0]
            else:
                return self.uppers[0]
        else:
            return (self.uppers[0]-self.lowers[0])/2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''