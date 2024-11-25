class UndergroundSystem:

    def __init__(self):
        self.time_collector = {}
        self.user_collector = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_collector.update({id: {"stationName":stationName,"time":t}})
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.user_collector:
            start=self.user_collector[id]["stationName"]
            if (start,stationName) not in self.time_collector:
                self.time_collector.update({(start,stationName):[t-self.user_collector[id]["time"]]})
            else:
                self.time_collector[(start,stationName)].append(t-self.user_collector[id]["time"])
            self.user_collector.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) in self.time_collector:
            return sum(self.time_collector[(startStation,endStation)])/len(self.time_collector[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)