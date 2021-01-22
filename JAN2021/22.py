#attempt3: Used dict->people used Counter for speed
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        if word1==word2 or sorted(word1)==sorted(word2):
            return True
        if len(word1)==1:
            return False
        a1=[0]*26
        a2=[0]*26
        ep1=[0]*26
        ep2=[0]*26
        for i in range(len(word1)):
            a1[ord(word1[i])-97]+=1
            a2[ord(word2[i])-97]+=1
            ep1[ord(word1[i])-97]=1
            ep2[ord(word2[i])-97]=1
        if ep1==ep2 and sorted(a1)==sorted(a2):
            return True
        return False
        

#attempt2: terrible performance
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        if word1==word2 or sorted(word1)==sorted(word2):
            return True
        if len(word1)==1:
            return False
        a1=[0]*26
        a2=[0]*26
        ep1=[0]*26
        ep2=[0]*26
        for i in range(len(word1)):
            a1[ord(word1[i])-97]+=1
            a2[ord(word2[i])-97]+=1
            ep1[ord(word1[i])-97]=1
            ep2[ord(word2[i])-97]=1
        if ep1==ep2 and sorted(a1)==sorted(a2):
            return True
        return False
'''

#attempt1:WA didn't think of strings where counts might be same but characters different
#example: uua and cbb would give true
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        if word1==word2 or sorted(word1)==sorted(word2):
            return True
        if len(word1)==1:
            return False
        a1=[0]*26
        a2=[0]*26
        for i in range(len(word1)):
            a1[ord(word1[i])-97]+=1
            a2[ord(word2[i])-97]+=1
        if sorted(a1)==sorted(a2):
            return True
        return False
'''
