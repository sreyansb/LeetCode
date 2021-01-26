#attempt1:
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        def findlen(di,le=1):
            maxie=0
            for i in di:
                if i=='#':
                    return le+1
                maxie+=findlen(di[i],le+1)
            return maxie
        
        di={}
        for i in words:
            k=di
            for j in i[::-1]:
                if j not in k:
                    k[j]={}
                k=k[j]
                if '#' in k:
                    del k['#']
            if len(k.keys())<1:
                k['#']=1
        
        sumi=0
        for i in di:
            j=findlen(di[i])
            #print(i,j)
            sumi+=j
        return sumi
        
        
