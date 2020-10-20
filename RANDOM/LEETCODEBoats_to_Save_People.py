#attempt2: 30% and 90%
class Solution:
    def numRescueBoats(self, people: List[int], k: int) -> int:
        count=0
        di={}
        people.sort()
        for i in people:
            if abs(i-k) in di:
                count+=1
                di[abs(i-k)]-=1
                if di[abs(i-k)]==0:
                    del di[abs(i-k)]
                continue
            if i not in di:
                di[i]=0
            di[i]+=1
        arr=list(di.keys())
        arr.sort()
        initptr=0
        lastptr=len(arr)-1
        while(initptr<=lastptr):
            if arr[initptr]+arr[lastptr]<=k:
                if (initptr!=lastptr):
                    count+=1
                    di[arr[initptr]]-=1
                    di[arr[lastptr]]-=1
                    if di[arr[initptr]]==0:
                        del di[arr[initptr]]
                        initptr+=1
                    if di[arr[lastptr]]==0:
                        del di[arr[lastptr]]
                        lastptr-=1
                elif (initptr==lastptr and di[arr[initptr]]>1):
                    count+=1
                    di[arr[initptr]]-=2
                    if di[arr[initptr]]==0:
                        del[di[arr[initptr]]]
                        initptr+=1
                else:
                    initptr+=1
            else:
                count+=di[arr[lastptr]]
                del di[arr[lastptr]]
                lastptr-=1
        for i in di:
            count+=di[i]
        return count

#attempt1: TLE 3/77 - because initptr==lastptr and then the code crashed
"""
class Solution:
    def numRescueBoats(self, people: List[int], k: int) -> int:
        count=0
        di={}
        people.sort()
        for i in people:
            if abs(i-k) in di:
                count+=1
                di[abs(i-k)]-=1
                if di[abs(i-k)]==0:
                    del di[abs(i-k)]
                continue
            if i not in di:
                di[i]=0
            di[i]+=1
        arr=list(di.keys())
        arr.sort()
        initptr=0
        lastptr=len(arr)-1
        while(initptr<=lastptr):
            if arr[initptr]+arr[lastptr]<=k:
                count+=1
                di[arr[initptr]]-=1
                di[arr[lastptr]]-=1
                if di[arr[initptr]]==0:
                    del di[arr[initptr]]
                    initptr+=1
                if di[arr[lastptr]]==0:
                    del di[arr[lastptr]]
                    lastptr-=1
            else:
                count+=di[arr[lastptr]]
                del di[arr[lastptr]]
                lastptr-=1
        for i in di:
            count+=di[i]
        return count
"""
