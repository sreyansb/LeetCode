#took help
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        di={}
        for i in tasks:
            if i not in di:
                di[i]=0
            di[i]+=1
        k=sorted(di.values())
        max_occurence=k[-1]
        counts=0
        for i in k[::-1]:
            if i!=max_occurence:
                break
            counts+=1
        return max(len(tasks),(max_occurence-1)*(n+1)+counts)
            
                
