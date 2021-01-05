#attempt1:
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not(customers):
            return 0
        n=len(customers)
        aver=0
        entrytime=0
        for i in customers:
            entrytime=max(i[0],entrytime)
            aver+=(i[1]+entrytime-i[0])
            #print(aver)
            entrytime=entrytime+i[1]
        return aver/n
        
        
