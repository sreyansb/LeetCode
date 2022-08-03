#attempt2: Used the n^2 algo
from bisect import bisect_left
from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.events = []
        self.leng = 0

    def book(self, start: int, end: int) -> bool:
        for event_start,event_end in self.events:
            if event_start == start or event_end == end or (event_start<start<event_end) or (event_start<end<event_end) or (start<event_start<end) or (start<event_end<end):
                return False
        self.events.append((start,end))
        return True
            
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
