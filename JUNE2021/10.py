#attempt2: Insert into an ordered list sort of array
class MyCalendar:
    
    def __init__(self):
        self.li=[]
        self.curlen=0

    def book(self, start: int, ends: int) -> bool:
        if self.curlen==0:
            self.curlen=1
            self.li.append((start,ends))
            return True
        parent=-1
        end=0
        while(end<self.curlen):
            if self.li[end][0]>=ends:
                break
            parent=end
            end=end+1
        if parent==-1:
            if start>=self.li[end][0]:
                return False
            self.li=[(start,ends)]+self.li
            self.curlen+=1
            return True
        if end==self.curlen:
            if self.li[parent][0]<start and self.li[parent][1]<=start:
                self.li.append((start,ends))
                self.curlen+=1
                return True
            return False
        if start>=self.li[parent][-1] and self.li[end][0]>start and self.li[end][0]>=ends:
            self.li=self.li[:end]+[(start,ends)]+self.li[end:]
            self.curlen+=1
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

#attempt1: WA because didnt take into consideration: that end of an interval has to be considered for adding inttervals
#didnt add things properly into the list
'''
from bisect import bisect_right
class MyCalendar:
    
    def __init__(self):
        self.li=[]
        self.di={}
        self.curlen=0
    
    def book(self, start: int, end: int) -> bool:
        pos=bisect_right(self.li,start)
        if pos==self.curlen:
            if self.curlen==0:
                self.li.append(start)
                self.di[self.curlen]=end
                self.curlen+=1
                return True
            else:
                if start>self.li[pos-1] and start>=self.di[pos-1]:
                    self.li.append(start)
                    self.di[self.curlen]=end
                    self.curlen+=1
                    return True
                return False
        else:
            if start>self.li[pos-1] and start>=self.di[pos-1] and start<self.li[pos] and start<self.di[pos]:
                self.li.append(start)
                self.di[self.curlen]=end
                self.curlen+=1
                return True
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
'''