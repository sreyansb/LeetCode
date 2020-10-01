#Attempt5: 30%
class RecentCounter:

    def __init__(self):
        self.arr=[]

    def ping(self, t: int) -> int:
        self.arr.append(t)
        i=0
        while(i<len(self.arr) and t-self.arr[i]>3000):
            i+=1
        self.arr=self.arr[i:]
        return len(self.arr)
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#Attempt4-> Accepted 5% window based approach
"""
class RecentCounter:

    def __init__(self):
        self.arr=[]
        self.l=0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        self.l+=1
        i=self.l-1
        while(i>-1 and t-self.arr[i]<=3000):
            i-=1
        return self.l-1-i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
""""

#Attempt 1,2,3 -> Runtime Error because the constraints given were wrong
"""
class RecentCounter:

    def __init__(self):
        self.arr=[]
        self.l=0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        self.l+=1
        i=self.l-1
        while(i>-1 and t-self.arr[i]<=3000):
            i-=1
        return self.l-1-i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
"""
