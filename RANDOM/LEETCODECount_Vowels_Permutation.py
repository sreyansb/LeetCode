#attempt1:
#have encoding: a=0, e=1,.., u=4
#and solve using that using dp
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dpt=[[-1 for i in range(5)]for j in range(n+1)]
        def dp(n,la=5):
            if n==0:
                return 0
            if n==1:
                if la==0 or la==4:
                    return 1
                elif la==1 or la==3:
                    return 2
                elif la==2:
                    return 4
                else:
                    return 5
            if la<5:
                if dpt[n][la]!=-1:
                    return dpt[n][la]
            temp=0
            if la<5:
                if la==0:
                    temp+=dp(n-1,1)
                elif la==1:
                    temp+=dp(n-1,0)
                    temp+=dp(n-1,2)
                elif la==2:
                    temp+=dp(n-1,0)
                    temp+=dp(n-1,1)
                    temp+=dp(n-1,3)
                    temp+=dp(n-1,4)
                elif la==3:
                    temp+=dp(n-1,2)
                    temp+=dp(n-1,4)
                elif la==4:
                    temp+=dp(n-1,0)
                dpt[n][la]=temp
                return temp
            else:
                for i in range(5):
                    tempi=dp(n-1,i)
                    dpt[n][i]=tempi
                return sum(dpt[n])%(10**9+7)
        return dp(n)
            
