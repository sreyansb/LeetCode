#attempt1:
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        di = {"a":["e"],"e":["a","i"],"i":["a","e","o","u"],"o":["i","u"],"u":["a"],"p":["a","e","i","o","u"]}
        mod = 1000000007
        @lru_cache(None)
        def find_permutations(n,past):
            if n==0:
                return 1
            ans = 0
            for next_char in di[past]:
                ans += find_permutations(n-1,next_char)
            return ans%mod
        return find_permutations(n,"p")
