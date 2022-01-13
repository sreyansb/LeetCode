#attempt1:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort(key=lambda x:(x[0],x[1]))
        xs,xe = points[0]
        for x1,x2 in points[1:]:
            if x1>xe:
                ans += 1
                xs,xe = x1,x2
            else:
                xe = min(xe,x2)
        return ans
