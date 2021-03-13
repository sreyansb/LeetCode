#attempt1:TOOK HELP.
#In such problems, simply use backtracking and solve
#give position in the answer and backtrack if further calls return False
'''
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans=[0]*(2*n-1)
        occurences=[2]*(n+1)
        occurences[1]=1
        visited=set(range(1,n+1))
        def backtrack(index):
            if index==2*n-1:
                return True
            if ans[index]:
                return backtrack(index+1)
            for i in range(n,0,-1):
                if i in visited:
                    if i==1:
                        ans[index]=i
                        visited.remove(i)
                        j=backtrack(index+1)
                        if not j:
                            ans[index]=0
                            visited.add(i)
                        else:
                            return j
                    else:
                        if index+i<2*n-1 and ans[index+i]==0:
                            ans[index]=ans[index+i]=i
                            visited.remove(i)
                            j=backtrack(index+1)
                            if not j:
                                ans[index]=ans[index+i]=0
                                visited.add(i)
                            else:
                                return j
            return False
        backtrack(0)
        return ans
'''
