#attempt2: sort based on points[i][1] as the major basis
#because if initial point is greater than end point of init then it wont ever be able to be shot by the arrow
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[1],x[0]))
        n=len(points)
        if n==0:
            return 0
        ans=1
        init=points[0]
        for i in range(1,n):
            if points[i][0]>init[1]:
                ans+=1
                init=points[i]
        return ans

#attempt1: WA-it is not a simple scheduling problem
#arrows are shot up towards the sky and not towards the Y -axis
#So we can't simply sort and check
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #we need to sort by points[i][1] as the main one
        points.sort(key=lambda x:(x[0],x[1]))
        n=len(points)
        if n==0:
            return 0
        ans=1
        init=points[0]
        for i in range(1,n):
            if points[i][0]>init[1]:#effectively means point cannot be burst
                #by any arrow from init
                ans+=1
                init=points[i]
        return ans
"""      
