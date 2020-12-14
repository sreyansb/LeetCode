#attempt1: TOOK HELP
#had an idea - do palindrome for each breaking point
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False for i in range(n)] for i in range(n)]
        #dp[i][j] represents if string[i:j+1] is a palindrome
        for i in range(n):
            dp[i][i]=True
        result=[]
        def recur(left,curlist):
            if left>=n:
                result.append(curlist.copy())
                #print(result)
            for end in range(left,n):
                if s[left]==s[end] and (end-left+1<=2 or dp[left+1][end-1]):
                    dp[left][end]=True
                    curlist.append(s[left:end+1])
                    recur(end+1,curlist)
                    curlist.pop()
        recur(0,[])
        return result
                
        
        
