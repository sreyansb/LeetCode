#attempt2 : COPIED
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.data = SortedDict({})

    def book(self, start: int, end: int) -> int:
        self.data.setdefault(start, 0)
        self.data.setdefault(end, 0)
        self.data[start] += 1
        self.data[end] -= 1

        ans = 0
        cur = 0
        for key in self.data:
            cur += self.data[key]
            ans = max(ans, cur)
        print(self.data)
        
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
