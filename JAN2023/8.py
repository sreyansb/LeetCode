#attempt3:
from fractions import Fraction
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        maxAns = 1
        for index1 in range(n):
            ySame = (0,points[index1][1])
            xSame = (float('inf'),points[index1][0])
            mapLines = {xSame: 1, ySame: 1 }
            for index2 in range(index1+1,n):
                if points[index1][0] == points[index2][0]:
                    mapLines[xSame] += 1
                    maxAns = max(maxAns, mapLines[xSame])
                elif points[index1][1] == points[index2][1]:
                    mapLines[ySame] += 1
                    maxAns = max(maxAns, mapLines[ySame])
                else:
                    slope = Fraction((points[index2][1]-points[index1][1]),(points[index2][0]-points[index1][0]))
                    constant = points[index2][1] - slope*points[index2][0]
                    if (slope, constant) not in mapLines:
                        mapLines[(slope,constant)]  = 1
                    mapLines[(slope,constant)]  += 1
                    maxAns = max(maxAns, mapLines[(slope,constant)])
                #print(mapLines)
        return maxAns

#attempt2: Forgot about issues with floating point
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        maxAns = 1
        for index1 in range(n):
            ySame = (0,points[index1][1])
            xSame = (float('inf'),points[index1][0])
            mapLines = {xSame: 1, ySame: 1 }
            for index2 in range(index1+1,n):
                if points[index1][0] == points[index2][0]:
                    mapLines[xSame] += 1
                    maxAns = max(maxAns, mapLines[xSame])
                elif points[index1][1] == points[index2][1]:
                    mapLines[ySame] += 1
                    maxAns = max(maxAns, mapLines[ySame])
                else:
                    slope = (points[index2][1]-points[index1][1])/(points[index2][0]-points[index1][0])
                    constant = points[index2][1] - slope*points[index2][0]
                    if (slope, constant) not in mapLines:
                        mapLines[(slope,constant)]  = 1
                    mapLines[(slope,constant)]  += 1
                    maxAns = max(maxAns, mapLines[(slope,constant)])
        return maxAns
'''

#attempt1:
