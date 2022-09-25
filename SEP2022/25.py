#attempt1:
class MyCircularQueue:

    def __init__(self, k: int):
        self.curlen = k+1
        self.rear = 0
        self.front = 0
        self.array = [-1]*(self.curlen)
        

    def enQueue(self, value: int) -> bool:
        #print(self.array,self.front,self.rear)
        if self.isFull():
            return False
        self.array[self.rear] = value
        self.rear = (self.rear+1)%self.curlen
        return True        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front+1)%self.curlen
        return True
        

    def Front(self) -> int:
        #print(self.array,self.front)
        if self.isEmpty():
            return -1
        return self.array[self.front]
        
    def Rear(self) -> int:
        #print(self.array,self.rear)
        if self.isEmpty():
            return -1
        return self.array[(self.rear-1+self.curlen)%self.curlen]
        

    def isEmpty(self) -> bool:
        ans = self.front == self.rear
        if ans:
            self.front = self.rear = 0
        return ans
        
    def isFull(self) -> bool:
        return (self.rear+1)%self.curlen == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
