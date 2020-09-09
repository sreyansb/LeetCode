#attempt4:heaps and all and other errors addressed 93.05%
from random import randrange
from heapq import heappush,heappop,heapify
class RandomizedCollection:

    def __init__(self):
        self.n=0
        self.l=[]
        self.di={}
        
    def insert(self, val: int) -> bool:
        if val not in self.di:
            self.di[val]=[-self.n]
            heapify(self.di[val])
            self.l.append(val)
            self.n+=1
            return True
        heappush(self.di[val],-self.n)
        self.l.append(val)
        self.n+=1
        return False       
        
    def remove(self, val: int) -> bool:
        if val not in self.di or not(self.di[val]):
            return False
        k=-1*self.di[val][0]
        self.l[k]=self.l[-1]
        heappop(self.di[self.l[k]])
        heappush(self.di[self.l[k]],-k)
        heappop(self.di[val])
        self.l[-1]=val
        self.l.pop()
        self.n-=1
        return True
        

    def getRandom(self) -> int:
        k=randrange(0,self.n)
        return self.l[k]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


#attempt 1 - run time error
#if only 1 element then massive error in remove
"""
from random import randrange
class RandomizedCollection:

    def __init__(self):
        self.n=0
        self.l=[]
        self.di={}
        

    def insert(self, val: int) -> bool:
        if val not in self.di:
            self.di[val]=[self.n]
            self.l.append(val)
            self.n+=1
            return True
        self.di[val].append(self.n)
        self.n+=1
        return False       
        
    def remove(self, val: int) -> bool:
        if val not in self.di:
            return False
        k=self.di[val].pop()
        self.l[k]=self.l[-1]
        self.di[self.l[k]].pop()
        self.di[self.l[k]].append(k)
        self.l[-1]=val
        self.l.pop()
        self.n-=1
        return True
        

    def getRandom(self) -> int:
        k=randrange(0,self.n)
        return self.l[k]
"""
