#attempt2:to prevent sorting and do stuff - 48% and 89%
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        if not(len(trips)):
            return True
        maxtime=1000
        ends=[[] for _ in range(maxtime+1)]
        starts=[[] for _ in range(maxtime+1)]
        for i in range(len(trips)):
            starts[trips[i][1]].append(i)
            ends[trips[i][-1]].append(i)
        curcapacity=0
        for i in range(1,maxtime+1):
            if curcapacity>capacity:
                return False
            if ends[i]:#first has to be ends because process might end before
            #a new process starts
                for j in ends[i]:
                    curcapacity-=trips[j][0]
            if starts[i]:
                for j in starts[i]:
                    curcapacity+=trips[j][0]
        if curcapacity>capacity:#very important condition->3rd test case
            return False
        return True


#attempt1: 60% and 30%
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        if not(len(trips)):
            return True
        
        trips.sort(key=lambda x:(x[-1],x[-2]))
        maxtime=trips[-1][-1]
        ends=[[] for _ in range(maxtime+1)]
        starts=[[] for _ in range(maxtime+1)]
        for i in range(len(trips)):
            starts[trips[i][1]].append(i)
            ends[trips[i][-1]].append(i)
        curcapacity=0
        for i in range(1,maxtime+1):
            if curcapacity>capacity:
                return False
            if ends[i]:
                for j in ends[i]:
                    curcapacity-=trips[j][0]
            if starts[i]:
                for j in starts[i]:
                    curcapacity+=trips[j][0]
        if curcapacity>capacity:
            return False
        return True
"""       
