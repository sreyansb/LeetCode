#attempt3:
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans=set()
        di={n:i for i,n in enumerate(words)}
        for i in range(len(words)):
            curword=words[i]
            for prefixindex in range(len(curword)+1):
                if curword[:prefixindex]==curword[:prefixindex][::-1]:
                    row=curword[prefixindex:][::-1]
                    if row in di and di[row]!=i:
                        ans.add((di[row],i))
            for suffixindex in range(len(curword),-1,-1):
                if curword[suffixindex:]==curword[suffixindex:][::-1]:
                    row=curword[:suffixindex][::-1]
                    if row in di and di[row]!=i:
                        ans.add((i,di[row]))
        ans=[list(i) for i in ans]
        return ans

#attempt2:TLE
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans=[]
        n=len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                k=words[i]+words[j]
                l=words[j]+words[i]
                leng=len(k)
                start,end,flag=0,leng-1,1
                while(start<=end):
                    if k[start]!=k[end]:
                        flag=0
                        break
                    start+=1
                    end-=1
                if flag:
                    ans.append([i,j])
                start,end,flag=0,leng-1,1
                while(start<=end):
                    if l[start]!=l[end]:
                        flag=0
                        break
                    start+=1
                    end-=1
                if flag:
                    ans.append([j,i])
                
        return ans
'''

#attempt1:TLE
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans=[]
        n=len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                k=words[i]+words[j]
                l=words[j]+words[i]
                if k==k[::-1]:
                    ans.append([i,j])
                if l==l[::-1]:
                    ans.append([j,i])
        return ans
'''