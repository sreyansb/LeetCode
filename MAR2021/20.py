#attempt1:
class UndergroundSystem:

    def __init__(self):
        self.trips={}
        self.checkedin={}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedin[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src=self.checkedin[id][0]
        tfull=t-self.checkedin[id][1]
        if src+stationName not in self.trips:
            self.trips[src+stationName]=(0,0)
        self.trips[src+stationName]=(self.trips[src+stationName][0]+1,self.trips[src+stationName][1]+tfull)
        del self.checkedin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t=self.trips[startStation+endStation]
        return t[1]/t[0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
