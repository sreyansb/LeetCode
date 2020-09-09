#2nd attempt - 66.67%
import random
class RandomizedSet:

    def __init__(self):
        self.n=0
        self.l=[]
        self.di={}
        
    def insert(self, val: int) -> bool:
        if val not in self.di:
            self.di[val]=self.n
            self.n+=1
            self.l.append(val)
            return True
        return False
            
    def remove(self, val: int) -> bool:
        if val in self.di:
            index=self.di[val]
            lastval=self.l[-1]
            self.di[lastval]=index
            self.l[index]=self.l[-1]
            self.l[-1]=val
            self.l.pop()
            del[self.di[val]]
            self.n-=1
            return True
        return False
        
    def getRandom(self) -> int:
        k=random.randint(0,self.n-1)
        return self.l[k]
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#1st attempt - 25%
"""
import random
class RandomizedSet:

    def __init__(self):
        self.n=0
        self.di={}
        
    def insert(self, val: int) -> bool:
        if val not in self.di:
            self.di[val]=1
            self.n+=1
            return True
        return False
            
    def remove(self, val: int) -> bool:
        if val in self.di:
            del(self.di[val])
            self.n-=1
            return True
        return False
        
    def getRandom(self) -> int:
        k=random.randint(0,self.n-1)
        return list(self.di.keys())[k]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""

