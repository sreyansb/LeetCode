#attempt1: blew up on the number of attempts
#two digits can appear continuously to make a single number
class Solution:
    def calculate(self, s: str) -> int:
        s=[i for i in s if i!=" "]
        if not(s):
            return
        m=['/','*','+','-']
        news=[s[0]]
        for i in s[1:]:
            if i not in m:
                if news[-1] not in m:
                    news[-1]+=i
                else:
                    news.append(i)
            else:
                news.append(i)
        s=news.copy()     
        #print(s)
        #to calculate divisions first
        for i in ['/*','+-']:
            news=[]
            n=len(s)
            j=0
            while(j<n):
                if s[j] in i:
                    k=int(news[-1])
                    if s[j]=='/':
                        news[-1]=str(k//int(s[j+1]))
                        j+=2
                    elif s[j]=='*':
                        news[-1]=str(k*int(s[j+1]))
                        j+=2
                    elif s[j]=='+':
                        news[-1]=str(k+int(s[j+1]))
                        j+=2
                    elif s[j]=='-':
                        news[-1]=str(k-int(s[j+1]))
                        j+=2
                else:
                    if j==0:
                        news.append(s[j])
                    elif s[j] not in m and news[-1] not in m:
                        news[-1]+=s[j]
                    elif s[j] in m or news[-1] in m:
                        news.append(s[j])
                    j+=1
            s=news.copy()
            #print(i,s)
        return int(s[-1])
