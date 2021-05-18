#attempt2: TOOK HELP: TUSHAR ROY CODING FULL EXPLANATION - SEE BOOK
from heapq import heappush,heappop,heapify
from functools import cmp_to_key
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        finarray=[]
        for i in buildings:
            finarray.append((i[0],i[2],'l'))
            finarray.append((i[1],i[2],'r'))
        def compare(item1,item2):
            if item1[0]<item2[0]:
                return -1
            elif item1[0]>item2[0]:
                return 1
            else:
                if item1[2]==item2[2]:
                    if item1[2]=='l':
                        return -1 if item1[1]>item2[1] else 1
                    else:
                        return -1 if item1[1]<item2[1] else 1
                else:
                    return -1 if item1[2]=='l' else 1
        finarray.sort(key=cmp_to_key(compare))
        #print(finarray)
        prior=[]
        heappush(prior,0)
        ans=[]
        for i in finarray:
            init=prior[0]
            if i[2]=='l':
                heappush(prior,-i[1])
            else:
                height=-i[1]
                pos=prior.index(height)
                prior=prior[:pos]+prior[pos+1:]
                heapify(prior)
            if prior[0]!=init:
                ans.append([i[0],-prior[0]])
            #print(i,ans)
            #print(prior)
        return ans
                
                
        

#attempt1:Didnt attempt,took help BD assignment
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        line=sorted((pos,tag,height,counterpart) for l,r,h in buildings 
                    for pos,tag,height,counterpart in [(l,'l',-h,r),(r,'r',-h,l)])
        prev_h,skyline,h_index=0,[],[(0,1<<32)]
        for p,t,h,c in line:
            if t=='l':
                heappush(h_index,(h,c))
            while h_index[0][1]<=p:
                heappop(h_index)
            h,_=h_index[0]
            if h!=prev_h:
                skyline.append((p,-h))
                prev_h=h
        return skyline
'''           
        
