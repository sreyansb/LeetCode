#attempt2: 70% very nice problem
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s=list(s)
        st=[[0,0]]
        for i in s:
            if st[-1][0]!=i:
                st.append([i,1])
            else:
                st[-1][1]+=1
                if st[-1][1]==k:
                    st.pop()
        return "".join([i[0]*i[1] for i in st[1:]])
            
#attempt1: TLE 17/18
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s=list(s)
        flag=1
        while(flag):
            #print(s)
            flag=0
            index=0
            new=[]
            n=len(s)
            while(index<=n-k):
                if len(set(s[index:index+k]))==1:
                    flag=1
                    index+=k
                else:
                    new.append(s[index])
                    index+=1
            new+=s[index:]
            if flag:
                s=new
        return "".join(s)
"""              
