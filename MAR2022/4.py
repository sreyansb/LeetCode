#aattempt3: 87ms
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        diprev = {}
        if query_glass>query_row:
            return 0
        if poured <= 1:
            return poured if (query_row,query_glass) == (0,0) else 0
        if (query_row,query_glass) == (0,0):
            return 1
        #diprev[x] stores the amount of liquid xth glass can send
        each_beak = (poured-1)/2
        diprev[0] = each_beak
        newdi = {}
        for currow in range(1,query_row):
            #print(sum(diprev.values()),diprev)
            limit = min(query_glass,currow)
            newdi[0] = diprev[0]
            if limit-1>=0:
                newdi[limit] = diprev[limit-1] + (diprev[limit] if limit in diprev else 0)
            for curcol in range(1,limit):
                newdi[curcol] = diprev[curcol-1]+diprev[curcol]
            diprev = newdi.copy()
            for i in diprev:
                if diprev[i] <= 1:
                    diprev[i] = 0
                else:
                    diprev[i] = (diprev[i]-1)/2
            
        newdi[0] = diprev[0] 
        limit = query_glass
        if limit-1>=0:
            newdi[limit] = diprev[limit-1] + (diprev[limit] if limit in diprev else 0)
        
        for curcol in range(1,limit):
            newdi[curcol] = diprev[curcol-1]+diprev[curcol]
        return min(1,newdi[query_glass])        

#attempt2: WA because of object allocation in Python
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        diprev = {}
        if query_glass>query_row:
            return 0
        if poured <= 1:
            return poured if (query_row,query_glass) == (0,0) else 0
        if (query_row,query_glass) == (0,0):
            return 1
        #diprev[x] stores the amount of liquid xth glass can send
        each_beak = (poured-1)/2
        diprev[0] = each_beak
        newdi = {}
        for currow in range(1,query_row):
            #print(diprev)
            limit = min(query_glass,currow)
            newdi[0] = diprev[0]
            if limit-1>=0:
                newdi[limit] = diprev[limit-1] + (diprev[limit] if limit in diprev else 0)
            for curcol in range(1,limit):
                newdi[curcol] = diprev[curcol-1]+diprev[curcol]
            diprev = newdi
            for i in diprev:
                if diprev[i] <= 1:
                    diprev[i] = 0
                else:
                    diprev[i] = (diprev[i]-1)/2
            
        newdi[0] = diprev[0] 
        limit = query_glass
        if limit-1>=0:
            newdi[limit] = diprev[limit-1] + (diprev[limit] if limit in diprev else 0)
        
        for curcol in range(1,limit):
            newdi[curcol] = diprev[curcol-1]+diprev[curcol]
        return min(1,newdi[query_glass])        
'''

#attempt1: WA because didn't consider the case of query_row,query_glass == 0,0
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        diprev = {}
        if query_glass>query_row:
            return 0
        if poured <= 1:
            return poured if (query_row,query_glass) == (0,0) else 0
        #diprev[x] stores the amount of liquid xth glass can send
        each_beak = (poured-1)/2
        diprev[0] = each_beak
        newdi = {}
        for currow in range(1,query_row):
            #print(diprev)
            limit = min(query_glass,currow)
            newdi[0] = diprev[0]
            if limit-1>=0:
                newdi[limit] = diprev[limit-1] + (diprev[limit] if limit in diprev else 0)
            for curcol in range(1,limit):
                newdi[curcol] = diprev[curcol-1]+diprev[curcol]
            diprev = newdi
            for i in diprev:
                if diprev[i] <= 1:
                    diprev[i] = 0
                else:
                    diprev[i] = (diprev[i]-1)/2
            
        newdi[0] = diprev[0] 
        limit = query_glass
        if limit-1>=0:
            newdi[limit] = diprev[limit-1] + (diprev[limit] if limit in diprev else 0)
        
        for curcol in range(1,limit):
            newdi[curcol] = diprev[curcol-1]+diprev[curcol]
        return min(1,newdi[query_glass])
'''
