#attempt6: TOOK HELP/HINT. Just maintain a a heap of all the fuel stations you have reached.
#if you are unable to reach a station: Just heappop the largest elements from the heap until you reach that particular station
#if you cant reach the station: return -1
#the last part is very important where we add curpos with startFUel and make it reach the target
'''
from heapq import heappush,heappop
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        index=0
        curpos=0
        number=0
        heap=[]
        while(index<len(stations) and curpos<target):
            if startFuel>=stations[index][0]-curpos:
                startFuel-=(stations[index][0]-curpos)
                heappush(heap,-stations[index][1])
                curpos=stations[index][0]
                index+=1
            else:
                if not(heap):
                    return -1
                startFuel+=-heappop(heap)
                number+=1
        curpos+=startFuel
        while(curpos<target):
            if not(heap):
                return -1
            curpos+=-heappop(heap)
            number+=1
        return number
'''

#attempt5: TLE 108/198
'''
from bisect import bisect_right
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        di={}
        stations.sort(key=lambda x:x[0])
        statloc=[]
        statfuel=[]
        for i in stations:
            statloc.append(i[0])
            statfuel.append(i[1])
        if not(statloc):
            return 0 if startFuel>=target else -1
        dpt={}
        def check(startFuel,curpos,statloc,statfuel):
            if curpos+startFuel>=target:
                return 0
            if (curpos,startFuel) in dpt:
                return dpt[(curpos,startFuel)]
            pos=bisect_right(statloc,curpos+startFuel)
            if pos==0:
                return float('inf')
            dpt[(curpos,startFuel)]=ans=float('inf')
            for i in range(pos):
                ans=min(ans,1+check(startFuel-(statloc[i]-curpos)+statfuel[i],statloc[i],statloc[i+1:],statfuel[i+1:]))
            dpt[(curpos,startFuel)]=ans
            return ans
        k=check(startFuel,0,statloc,statfuel)
        return -1 if k==float('inf') else k
'''

#attempt4: TLE 103/198 but works for all the cases which the previous ones weren't working for
'''
from bisect import bisect_right
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        di={}
        stations.sort(key=lambda x:x[0])
        statloc=[]
        statfuel=[]
        for i in stations:
            statloc.append(i[0])
            statfuel.append(i[1])
        if not(statloc):
            return 0 if startFuel>=target else -1
        nofuels=0
        curpos=0
        def check(startFuel,curpos,statloc,statfuel):
            if curpos+startFuel>=target:
                return 0
            pos=bisect_right(statloc,curpos+startFuel)
            if pos==0:
                return float('inf')
            ans=float('inf')
            for i in range(pos):
                ans=min(ans,1+check(startFuel-(statloc[i]-curpos)+statfuel[i],statloc[i],statloc[i+1:],statfuel[i+1:]))
            return ans
        k=check(startFuel,0,statloc,statfuel)
        return -1 if k==float('inf') else k
'''

#attempt3: DOESN"T WORK because you could go from position to next
'''
from bisect import bisect_right
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        di={}
        stations.sort(key=lambda x:x[0])
        statloc=[]
        statfuel=[]
        for i in stations:
            statloc.append(i[0])
            statfuel.append(i[1])
        if not(statloc):
            return 0 if startFuel>=target else -1
        nofuels=0
        curpos=0
        while(startFuel and curpos+startFuel<target):
            
            pos=bisect_right(statloc,curpos+startFuel)
            if pos==0:
                return -1
            maxie,index=0,-1
            if pos!=len(statloc):
                val=statloc[pos]
            else:
                val=target
            #print(startFuel,curpos,pos)
            for i in range(pos):
                if curpos+startFuel-statloc[i]+statloc[i]+statfuel[i]>=val and curpos+startFuel-statloc[i]+statloc[i]+statfuel[i]>=maxie:
                    index=i
                    maxie=max(maxie,curpos+startFuel-statloc[i]+statloc[i]+statfuel[i])
            if index==-1:
                return -1
            fuelspent=+statloc[index]-curpos
            startFuel=startFuel-fuelspent+statfuel[index]
            nofuels+=1
            curpos=statloc[index]
            statloc=statloc[index+1:]
            statfuel=statfuel[index+1:]
            
        return nofuels if curpos+startFuel>=target else -1
'''

#attempt2: WA Thought of taking the fuel sation which gives the most bang for the buck i.e. fuel spent is the least and added fuel is highest.
#doesn't work for :1000 299 [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
'''
from bisect import bisect_right
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        di={}
        stations.sort(key=lambda x:x[0])
        statloc=[]
        statfuel=[]
        for i in stations:
            statloc.append(i[0])
            statfuel.append(i[1])
        if not(statloc):
            return 0 if startFuel>=target else -1
        nofuels=0
        curpos=0
        while(startFuel and curpos+startFuel<target):
            pos=bisect_right(statloc,curpos+startFuel)
            if pos==0:
                return -1
            maxie,index=0,-1
            for i in range(pos):
                if startFuel+statloc[i]-curpos+statfuel[i]>=maxie:
                    index=i
                    maxie=max(maxie,startFuel+statloc[i]-curpos+statfuel[i])
            fuelspent=+statloc[index]-curpos
            startFuel=startFuel-fuelspent+statfuel[index]
            nofuels+=1
            curpos=statloc[index]
            statloc=statloc[index+1:]
            statfuel=statfuel[index+1:]   
            
        return nofuels if curpos+startFuel>=target else -1
'''

#attempt1: WA:166/198 THOUGHT OF TAKING THE fuel station which gives the most fuel: Wrong Idea
'''
from bisect import bisect_right
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        di={}
        stations.sort(key=lambda x:x[0])
        statloc=[]
        statfuel=[]
        for i in stations:
            statloc.append(i[0])
            statfuel.append(i[1])
        if not(statloc):
            return 0 if startFuel>=target else -1
        nofuels=0
        curpos=0
        while(startFuel and curpos+startFuel<target):
            pos=bisect_right(statloc,curpos+startFuel)
            print(curpos,statloc,startFuel,pos)
            if pos==0:
                return -1
            maxie,index=0,-1
            for i in range(pos):
                if statfuel[i]>=maxie:
                    index=i
                    maxie=max(maxie,statfuel[i])
            fuelspent=+statloc[index]-curpos
            startFuel=startFuel-fuelspent+statfuel[index]
            nofuels+=1
            curpos=statloc[index]
            statloc=statloc[index+1:]
            statfuel=statfuel[index+1:]   
            
            
        return nofuels if curpos+startFuel>=target else -1
        
'''