#attempt3:AC
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        distfroml=[float('inf') for i in range(n)]
        prevpos=float('inf')
        if dominoes[-1]=='L':
            prevpos=n-1
            distfroml[-1]=0
        for i in range(n-2,-1,-1):
            if dominoes[i]=='R':
                prevpos=float('inf')
                distfroml[i]=float('inf')
            elif dominoes[i]=='L':
                prevpos=i
                distfroml[i]=0
            else:
                distfroml[i]=prevpos-i
        prevposr=float('inf')
        distfromr=[float('inf') for i in range(n)]
        if dominoes[0]=='R':
            prevposr=0
            distfromr[0]=0
        for i in range(1,n):
            if dominoes[i]=='L':
                prevposr=float('inf')
                distfromr[i]=float('inf')
            elif dominoes[i]=='R':
                prevposr=i
                distfromr[i]=0
            else:
                distfromr[i]=i-prevposr
        #print(distfroml)
        #print(distfromr)
        finalans=""
        for i in range(n):
            if distfromr[i]==distfroml[i]:
                finalans+="."
            elif distfromr[i]<distfroml[i]:
                if distfromr[i]!=-float('inf'):
                    finalans+="R"
                else:
                    if distfroml[i]==float('inf'):
                        finalans+="."
                    else:
                        finalans+="L"
            else:
                finalans+="L"
        return finalans

#attempt2: WA Oversight: WHaile making finalans in distfromr[i]<distfroml[i] made the if else condition
#have the same output for any condition
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        distfroml=[float('inf') for i in range(n)]
        prevpos=float('inf')
        if dominoes[-1]=='L':
            prevpos=n-1
            distfroml[-1]=0
        for i in range(n-2,-1,-1):
            if dominoes[i]=='R':
                prevpos=float('inf')
                distfroml[i]=float('inf')
            elif dominoes[i]=='L':
                prevpos=i
                distfroml[i]=0
            else:
                distfroml[i]=prevpos-i
        prevposr=float('inf')
        distfromr=[float('inf') for i in range(n)]
        if dominoes[0]=='R':
            prevposr=0
            distfromr[0]=0
        for i in range(1,n):
            if dominoes[i]=='L':
                prevposr=float('inf')
                distfromr[i]=float('inf')
            elif dominoes[i]=='R':
                prevposr=i
                distfromr[i]=0
            else:
                distfromr[i]=i-prevposr
        #print(distfroml)
        #print(distfromr)
        finalans=""
        for i in range(n):
            if distfromr[i]==distfroml[i]:
                finalans+="."
            elif distfromr[i]<distfroml[i]:
                if distfromr[i]!=-float('inf'):
                    finalans+="R"
                else:
                    if distfroml[i]==float('inf'):
                        finalans+="."
                    else:
                        finalans+="."
            else:
                finalans+="L"
        return finalans
''' 

#attempt1: WA distfroml has to be made float('inf') for correct stuff
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        distfroml=[n for i in range(n)]
        prevpos=float('inf')
        if dominoes[-1]=='L':
            prevpos=n-1
            distfroml[-1]=0
        for i in range(n-2,-1,-1):
            if dominoes[i]=='R':
                prevpos=float('inf')
                distfroml[i]=float('inf')
            elif dominoes[i]=='L':
                prevpos=i
                distfroml[i]=0
            else:
                distfroml[i]=prevpos-i
        prevposr=float('inf')
        distfromr=[float('inf') for i in range(n)]
        if dominoes[0]=='R':
            prevposr=0
            distfromr[0]=0
        for i in range(1,n):
            if dominoes[i]=='L':
                prevposr=float('inf')
                distfromr[i]=float('inf')
            elif dominoes[i]=='R':
                prevposr=i
                distfromr[i]=0
            else:
                distfromr[i]=i-prevposr
        #print(distfroml)
        #print(distfromr)
        finalans=""
        for i in range(n):
            if distfromr[i]==distfroml[i]:
                finalans+="."
            elif distfromr[i]<distfroml[i]:
                if distfromr[i]!=-float('inf'):
                    finalans+="R"
                else:
                    if distfroml[i]==float('inf'):
                        finalans+="."
                    else:
                        finalans+="."
            else:
                finalans+="L"
        return finalans
'''