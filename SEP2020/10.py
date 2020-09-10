#attempt 2: 97% 32ms
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i=0
        n=len(secret)
        secret,guess=list(secret),list(guess)
        bulls=0
        cows=0
        poss=[]
        while(i<n):
            if secret[i]==guess[i]:
                bulls+=1
                guess[i]=""
                secret[i]=""
            i+=1
        sec={}
        gue={}
        for i in guess:
            if i!="":
                if i not in gue:
                    sec[i]=0
                    gue[i]=0
                gue[i]+=1
        for i in secret:
            if i!="":
                if i not in sec :
                    sec[i]=0
                sec[i]+=1
        for j in gue:
            cows+=min(gue[j],sec[j])
        
        return f"{bulls}A{cows}B"

#attempt1: very very slow 620ms
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        i=0
        n=len(secret)
        secret,guess=list(secret),list(guess)
        bulls=0
        cows=0
        poss=[]
        while(i<n):
            if secret[i]==guess[i]:
                bulls+=1
                guess[i]=""
            else:
                poss.append(secret[i])
            i+=1
        for i in poss:
            for j in range(n):
                if i==guess[j]:
                    cows+=1
                    guess[j]=""
                    break
        return f"{bulls}A{cows}B"
"""
