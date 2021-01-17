#attempt1:
class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==0:
            return 0
        def recurse(leng,string=""):
            if leng==0:
                return 1
            res=0
            if string:
                for i in ["a","e","i","o","u"][::-1]:
                    if i<string[0]:
                        break
                    res+=recurse(leng-1,i+string)
            else:
                for i in ["a","e","i","o","u"]:
                    res+=recurse(leng-1,i)
            return res
        return recurse(n)
        
