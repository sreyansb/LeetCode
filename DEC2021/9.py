#attempt1:
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def findex(curindex,visited=set()):
            if arr[curindex] == 0:
                return True
            visited.add(curindex)
            ans = False
            if curindex+arr[curindex]<n and curindex+arr[curindex] not in visited:
                ans = findex(curindex+arr[curindex],visited)
            if ans:
                return ans
            if curindex-arr[curindex]>-1 and curindex-arr[curindex] not in visited:
                return findex(curindex-arr[curindex],visited)
        return findex(start)
