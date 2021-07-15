#attempt1:
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curlen=len(words[0])
        lastindices=[]
        n=len(words)
        for i in range(1,n):
            if curlen+len(words[i])+1>maxWidth:
                lastindices.append((i-1,curlen))
                curlen=0
            if curlen:
                curlen+=len(words[i])+1
            else:
                curlen=len(words[i])
        lastindices.append((n-1,curlen))
        previndex=0
        ans=[]
        for i in lastindices[:-1]:
            curlen=i[1]
            try:
                nosp=(maxWidth-curlen)//(i[0]-previndex)
            except:
                nosp=(maxWidth-curlen)
            chartojoin=" "*(nosp+1)
            spacesremaining=maxWidth-(curlen+nosp*(i[0]-previndex))
            stringtoappend=chartojoin.join(words[previndex:i[0]+1]).replace(chartojoin," "*(nosp+2),spacesremaining)
            stringtoappend=stringtoappend+" "*(maxWidth-len(stringtoappend))
            ans.append(stringtoappend)
            #print(stringtoappend,nosp,len(stringtoappend),spacesremaining)
            previndex=i[0]+1
        curlen=lastindices[-1][1]
        #print(curlen)
        ans.append(" ".join(words[previndex:lastindices[-1][0]+1])+" "*(maxWidth-curlen))
        return ans
        
        
    
        
            
        