#attempt3:
class MyCircularQueue:

    def __init__(self, k: int):
        self.front=-1
        self.end=-1
        self.len=k+1
        self.arr=[-1]*(k+1)

    def enQueue(self, value: int) -> bool:
        if self.front==-1:
            self.front=0
            self.end=0
        if (self.end+1)%self.len==self.front:
            return False
        self.arr[(self.end+1)%self.len]=value
        self.end=(self.end+1)%self.len
        
        return True

    def deQueue(self) -> bool:
        if self.end==self.front:
            return False
        self.front=(self.front+1)%self.len
        return True

    def Front(self) -> int:
        
        if not(self.isEmpty()):
            return self.arr[(self.front+1)%self.len]
        return -1

    def Rear(self) -> int:
        
        if not(self.isEmpty()):
                return self.arr[(self.end+self.len)%self.len]
        return -1
        
    def isEmpty(self) -> bool:
        
        return self.end==self.front

    def isFull(self) -> bool:
        
        return (self.end+1)%self.len==self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
