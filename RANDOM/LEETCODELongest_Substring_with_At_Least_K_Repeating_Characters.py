#attempt1: Took help
#Recursion based problem->very nice
#I thought of bucket sort and all->thought of a similar approach but didnt know
#how to apply.
#RECURSION IT IS
#took help in clues: Tutorials Point
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def recurse(s,k):
            #print(s,k)
            n=len(s)
            if k>n:
                return 0
            if k==1:
                return n
            buckets=[0 for i in range(26)]
            for i in range(n):
                buckets[ord(s[i])-ord('a')]+=1
            badchar=""
            for i in range(26):
                if buckets[i]>0 and buckets[i]<k:
                    badchar=chr(i+ord('a'))
                    break
            if not(badchar):
                return n
            stringsofbadchar=s.split(badchar)
            maxie=0
            for i in stringsofbadchar:
                maxie=max(maxie,recurse(i,k))
            return maxie
        return recurse(s,k)
                
'''
#took help in clues: Tutorials Point
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def recurse(s):
            n=len(s)
            if not(n):
                return 0
            if n<k:
                return 0
            if k==1:
                return n
            buckets={}
            for i in s:
                if i not in buckets:
                    buckets[i]=0
                buckets[i]+=1
            badchar=""
            for i in buckets:
                if buckets[i]<k:
                    badchar=i
                    break
            if badchar=="":
                return n
            strings=s.split(badchar)
            ans=0
            for i in strings:
                ans=max(ans,recurse(i))
            return ans
        return recurse(s)
'''
                    
            
                    
        
            
        
