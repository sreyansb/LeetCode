#attempt1: greedy based on units works
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxtypes=[i for i in boxTypes if i[0]<=truckSize]
        n=len(boxtypes)
        boxtypes.sort(key=lambda x:-x[1])
        cursize=0
        ans=0
        index=0
        while(index<n and cursize<truckSize):
            curtruck=boxtypes[index]
            if cursize+curtruck[0]<=truckSize:
                cursize+=curtruck[0]
                ans+=curtruck[1]*curtruck[0]
            else:
                a=truckSize-cursize
                if a<0:
                    break
                cursize=truckSize
                ans+=a*curtruck[1]
            index+=1
        return ans