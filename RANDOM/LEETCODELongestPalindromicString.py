#Attempt2->Faster O(n^2) algo
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not(s) or len(s)==1:
            return s
        n=len(s)
        def expand(s,start,end):
            while(start>-1 and end<n and s[start]==s[end]):
                start-=1
                end+=1
            return s[start+1:end]
        final=s[0]
        for i in range(n):
            k=expand(s,i,i)
            #print(i,k)
            if len(k)>len(final):
                final=k
            k=expand(s,i,i+1)
            #print(i,k)
            if len(k)>len(final):
                final=k
        return final
"""
#1st attempt - Very slow O(n^3) solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        final=""
        n=len(s)
        for i in range(n):
            current=s[i]
            for j in range(i+1,n):
                k=s[i:j+1]
                if k==k[::-1]:
                    current=current if len(k)<len(current) else k
            final=final if len(final)>len(current) else current
        return final
"""


