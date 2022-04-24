#attempt1:
class UndergroundSystem:

    def __init__(self):
        self.checked_in_users = {} #maps userid to (sourcestation,starttime)
        self.station_time_map = {} #maps (sorcestn,deststn) tuple to list of times
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in_users[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checked_in_users:
            reqd_tuple = (self.checked_in_users[id][0],stationName)
            if reqd_tuple not in self.station_time_map:
                self.station_time_map[reqd_tuple] = []
            self.station_time_map[reqd_tuple].append(t-self.checked_in_users[id][1])
            del self.checked_in_users[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) in self.station_time_map:
            return sum(self.station_time_map[(startStation,endStation)])/len(self.station_time_map[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
