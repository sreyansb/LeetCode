#attempt1: 50%
class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in s:
            if i==']':
                k=""
                while(st[-1]!="["):
                    k=st.pop()+k
                st.pop()
                k=k*int(st.pop())
                st.append(k)
            else:
                if i.isnumeric():
                    if st and st[-1].isnumeric():
                        st[-1]+=i
                    else:
                        st.append(i)
                else:
                    st.append(i)
            #print(st)
        return "".join(st)
                
                
        
