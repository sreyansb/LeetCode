#attempt2:
from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.times = SortedList()
        self.time_key_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.time_key_map:
            self.time_key_map[timestamp] = {}
            self.times.add(timestamp)
        self.time_key_map[timestamp][key] = value        

    def get(self, key: str, timestamp: int) -> str:
        pos = self.times.bisect_right(timestamp)
        for index in range(pos-1,-1,-1):
            map_to_fetch = self.time_key_map[self.times[index]]
            if (key in map_to_fetch):
                return map_to_fetch[key]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#attempt1: WA
'''
from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.times = SortedList()
        self.time_key_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.time_key_map:
            self.time_key_map[timestamp] = {}
            self.times.add(timestamp)
        self.time_key_map[timestamp][key] = value        

    def get(self, key: str, timestamp: int) -> str:
        pos = self.times.bisect_right(timestamp)
        if pos == 0:
            return ""
        map_to_fetch = self.time_key_map[self.times[pos-1]]
        return map_to_fetch[key] if key in map_to_fetch else list(map_to_fetch.values())[0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
'''
