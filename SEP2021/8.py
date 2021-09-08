#attempt1:
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        finalstr="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"
        n=len(s)
        suffixsum=[0]*n
        suffixsum[-1]=shifts[-1]
        suffixsum[-1]%=26
        for i in range(n-2,-1,-1):
            suffixsum[i]=suffixsum[i+1]+shifts[i]
            suffixsum[i]%=26
        final=""
        for i in range(n):
            final+=finalstr[finalstr.index(s[i])+suffixsum[i]]
        return final
        
        