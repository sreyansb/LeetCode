#attempt1:
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        di = {}
        for i in range(n-1,-1,-1):
            if s[i] not in di:
                di[s[i]] = i
        ans = []
        i = 0
        while(i<n):
            rightmost = di[s[i]]
            index = i+1
            while(index<min(n,rightmost)):
                rightmost = max(rightmost,di[s[index]])
                index += 1
            ans.append(rightmost-i+1)
            i = rightmost+1
        return ans
        
        
