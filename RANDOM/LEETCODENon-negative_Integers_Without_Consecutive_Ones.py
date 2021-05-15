#attempt2:TOOK HELP DIGIT DP
class Solution:
    def findIntegers(self, n: int) -> int:
        n=str(bin(n))[2:]
        leng=len(n)
        
        @lru_cache(None)
        def dp(curlen,parent,tight):
            if curlen==leng:
                return 1
            upperbound=1
            if tight:
                upperbound=int(n[curlen])
            res=0
            for i in range(upperbound+1):
                if i==parent==1:
                    continue
                res+=dp(curlen+1,i,tight&(i==upperbound))
            return res
        return dp(0,-1,1)        

#attempt1: TLE
'''
class Solution:
    def findIntegers(self, n: int) -> int:
        if n<2:
            return 2
        binary=str(bin(n)[2:])
        zero={"0"}
        one={"1"}
        leng=2
        while(leng<=len(binary)):
            z=set()
            o=set()
            for i in zero:
                if i+"1"<=binary:
                    z.add((i+"1").lstrip("0"))
                if i+"0"<=binary:
                    o.add((i+"0").lstrip("0"))
            for i in one:
                if i+"0"<=binary:
                    o.add((i+"0").lstrip("0"))
            zero=zero|o
            one=one|z
            leng+=1
        k=zero|one
        #print(k)
        return len(k)-1
'''
