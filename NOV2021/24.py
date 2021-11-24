#attempt2:
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        starttime = [i[0] for i in secondList]
        ans = set()
        for i in firstList:
            for j in secondList:
                m1 = max(i[0],j[0])
                m2 = min(j[1],i[1])
                if m1>m2:
                    continue
                if i[0]<=i[1]<=j[1] or j[0]<=j[1]<=i[1]:
                    ans.add((m1,m2))
        return sorted(ans,key=lambda x:(x[0],x[1]))

#attempt1:WA because ans has to be a set and also sorted
'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        starttime = [i[0] for i in secondList]
        ans = []
        for i in firstList:
            for j in secondList:
                m1 = max(i[0],j[0])
                m2 = min(j[1],i[1])
                if m1>m2:
                    continue
                if i[0]<=i[1]<=j[1]:
                    ans.append([m1,m2])
                if j[0]<=j[1]<=i[1]:
                    ans.append([m1,m2])
        return ans
'''
