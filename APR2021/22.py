#attempt2: DIctionary, see every index where a brick ends and add it to the
#dictionary
from bisect import bisect_right
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        for i in range(len(wall)):
            for j in range(1,len(wall[i])):
                wall[i][j]+=wall[i][j-1]
        finalsum=wall[0][-1]
        di={}
        maxie=0
        for i in range(len(wall)):
            for j in wall[i][:-1]:
                if j not in di:
                    di[j]=0
                di[j]+=1
                maxie=max(maxie,di[j])
        return len(wall)-maxie

#attempt1:TLE because width can be INT_MAX and bisect_right!!!!!!!
'''
from bisect import bisect_right
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        for i in range(len(wall)):
            for j in range(1,len(wall[i])):
                wall[i][j]+=wall[i][j-1]
        finalsum=wall[0][-1]
        mini=len(wall)
        for i in range(1,finalsum):
            cursum=0
            #print("I: ",i)
            for j in range(len(wall)):
                pos=bisect_right(wall[j],i)
                if wall[j][pos-1]==i:
                    pass
                else:
                    cursum+=1
            #print(cursum)
            mini=min(mini,cursum)
        return mini
'''
