#Attempt2: AC 81%
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        k=-float('inf')
        for i in asteroids:
            #print(st)
            flag=0
            while(st):
                flag=0
                if st[-1]>0 and i<0:
                    flag=1
                    if st[-1]>-1*i:
                        k=-i
                        break
                    elif st[-1]<-i:
                        k=st.pop()
                    else:
                        st.pop()
                        flag=1
                        k=-i
                        break
                else:
                    break
            if (flag and k!=-i) or flag==0:
                st.append(i)
        return st
                
                        
                
                    
            
            

#attempt1:WA 208/272
#WA because if i==st[-1], curele cant be appended
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        k=-float('inf')
        for i in asteroids:
            flag=0
            while(st):
                flag=0
                if st[-1]>0 and i<0:
                    flag=1
                    if st[-1]>-1*i:
                        k=-i
                        break
                    elif st[-1]<-1*i:
                        k=st.pop()
                    else:
                        k=st.pop()
                else:
                    break
            if (flag and k!=-i) or flag==0:
                st.append(i)
        return st
            
"""
