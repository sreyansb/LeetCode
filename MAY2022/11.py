#attempt1:
class Solution:
    def countVowelStrings(self, n: int) -> int:
        answer_for_past = {'a':5,"e":4,"i":3,"o":2,"u":1}
        @lru_cache(None)
        def counter(nleft,pastvariable='a'):
            if nleft == 1:
                return answer_for_past[pastvariable]
            if pastvariable == 'a':
                return counter(nleft-1,"a")+counter(nleft-1,"e")+counter(nleft-1,"i")+counter(nleft-1,"o")+counter(nleft-1,"u")
            if pastvariable == 'e':
                return counter(nleft-1,"e")+counter(nleft-1,"i")+counter(nleft-1,"o")+counter(nleft-1,"u")
            if pastvariable == 'i':
                return counter(nleft-1,"i")+counter(nleft-1,"o")+counter(nleft-1,"u")
            if pastvariable == 'o':
                return counter(nleft-1,"o")+counter(nleft-1,"u")
            if pastvariable == 'u':
                return counter(nleft-1,"u")
        return counter(n)
                    
        
