#attempt1:
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def findans(n,parent):
            if n == 0:
                return [str(parent)]
            ans = []
            for nextElement in [parent+k,parent-k]:
                if 0<=nextElement<10:
                    nextAns = findans(n-1,nextElement)
                    for nextans in nextAns:
                        ans.append(str(parent)+nextans)
            return ans
        ans = []
        for number in range(1,10):
            answers = findans(n-1,number)
            ans.extend([int(answer) for answer in answers])
        return set(ans)
            
