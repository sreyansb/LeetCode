class TimeMap:

    def __init__(self):
        self.di={}
        self.di2={}
        

    def set(self, key: str, value: str, time: int) -> None:
        if key in self.di:
            self.di[key].append(time)
            self.di2[key].append(value)
        else:
            self.di[key]=[time]
            self.di2[key]=[value]
    def get(self, key: str, time: int) -> str:
        if key not in self.di:
            return ""
        position=bisect_right(self.di[key],time)
        return self.di2[key][position-1] if position else ""
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""
#very slow because of the sorting -> but something says that the timestamps were
#already sorted when pushed into the dictionary
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.di={}
        self.di2={}
        

    def set(self, key: str, value: str, time: int) -> None:
        if key in self.di:
            self.di[key].append(time)
            self.di[key].sort()
            self.di2[(key,time)]=value
        else:
            self.di[key]=[time]
            self.di2[(key,time)]=value
    def get(self, key: str, time: int) -> str:
        if key not in self.di:
            return ""
        position=bisect_right(self.di[key],time)
        return self.di2[(key,self.di[key][position-1])] if position!=0 else ""
            
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
