#attempt1: Compress the string and find the answers

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def strcompr(wordi):
            final=""
            i=0
            n=len(wordi)
            while(i<n):
                count=0
                temp=wordi[i]
                while(i<n and wordi[i]==temp):
                    count+=1
                    i+=1
                final=final+temp+str(count)
            return final
        def comparestr(i,pat):
            if len(i)!=len(pat):
                return False
            di={}
            di1=set()
            j=0
            n=len(i)
            while(j<n):
                if i[j].isalpha():
                    if pat[j].isalpha():
                        if i[j] in di:
                            if di[i[j]]!=pat[j]:
                                return False
                        else:
                            if pat[j] in di1:
                                return False
                            di1.add(pat[j])
                            di[i[j]]=pat[j]
                    else:
                        return False
                tempi=j+1
                while(tempi<n and i[tempi].isdigit()):
                    if i[tempi]!=pat[tempi]:
                        return False
                    tempi+=1
                j=tempi
                    
            return True
        finpat=strcompr(pattern)
        lid=[]
        ans=[]
        for i in words:
            lid.append(strcompr(i))
        #print(finpat,lid)
        for i in range(len(lid)):
            if comparestr(lid[i],finpat):
                ans.append(words[i])
        return ans