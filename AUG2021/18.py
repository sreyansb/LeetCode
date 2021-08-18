#attempt1:
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def recurse(index):
            if index>=n:
                return 1
            if s[index]=="0":
                return 0
            if s[index]=='1':
                if index+1<n:
                    if s[index+1]=="0":
                        return recurse(index+2)
                    else:
                        return recurse(index+1)+recurse(index+2)
                else:
                    return recurse(index+1)
            elif s[index]=='2':
                if index+1<n:
                    if s[index+1]=="0":
                        return recurse(index+2)
                    else:
                        if 1<=int(s[index+1])<=6:
                            return recurse(index+1)+recurse(index+2)
                        else:
                            return recurse(index+1)
                else:
                    return recurse(index+1)
            else:
                return recurse(index+1)
        return recurse(0)
        