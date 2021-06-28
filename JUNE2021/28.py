#attempt1:
class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans=[[0,0]]
        for i in S:
            if ans[-1][0]==i:
                ans[-1][1]+=1
                if ans[-1][1]==2:
                    ans.pop()
            else:
                ans.append([i,1])
        return "".join([i[0]*i[1] for i in ans[1:]])
