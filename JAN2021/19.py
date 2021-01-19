#attempt2: O(n^2) 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not(s):
            return 0
        maxl=1
        string=s[0]
        n=len(s)
        for i in range(1,n):
            j=0
            while(i-j>=0 and i+j<n):
                if s[i-j]==s[i+j]:
                    maxl=max(maxl,2*j+1)
                    if maxl==2*j+1:
                        string=s[i-j:i+j+1]
                    j+=1
                else:
                    break
            #very important for even length strings
            if s[i-1]==s[i]:
                maxl=max(2,maxl)
                if maxl==2:
                    string=s[i-1]+s[i]
                j=1
                while(i-j-1>=0 and i+j<n):
                    if s[i-1-j]==s[i+j]:
                        maxl=max(maxl,2*(j+1))
                        if maxl==2*j+2:
                            string=s[i-j-1:i+j+1]
                        j+=1
                    else:
                        break
        return string
        
#attempt1: TLE 138/174 n^2 algo with O(n) palindrome checking algo
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not(s):
            return 0
        maxl=1
        string=s[0]
        n=len(s)
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i:j+1]==s[i:j+1][::-1]:
                    maxl=max(maxl,j-i+1)
                    if maxl==j-i+1:
                        string=s[i:j+1]
        return string
'''
