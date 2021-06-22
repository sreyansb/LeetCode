#attempt1:
from bisect import bisect_left
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        di={}
        for i in range(len(s)):
            if s[i] not in di:
                di[s[i]]=[[],0]
            di[s[i]][0].append(i)
            di[s[i]][-1]+=1
        ans=0
        for i in words:
            if i[0] not in di:
                continue
            #we need to find out the leftmost occurence of the character after previous characters' occurence
            pos=di[i[0]][0][0]+1
            flag=1
            for character in i[1:]:
                if character not in di:
                    flag=0
                    break
                newpos=bisect_left(di[character][0],pos)
                if newpos==di[character][1]:
                    flag=0
                    break
                pos=di[character][0][newpos]+1
            ans+=flag
        return ans