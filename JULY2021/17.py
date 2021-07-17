#attempt6: AC 
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        nones=arr.count(1)
        if nones%3:
            return [-1,-1]
        nones=nones//3
        if nones==0:
            return [0,2]
        di={}
        count=0
        for i in range(len(arr)):
            if arr[i]:
                di[count+1]=i
                count+=1
            arr[i]=str(arr[i])
        arr="".join(arr)
        i=di[nones+1]
        j=di[2*nones+1]
        ans=[-1,-1]
        strreqd=arr[j:]
        try:
            ans[0]=arr[:i].index(strreqd)+len(strreqd)-1
        except:
            return ans
        try:
            ans[1]=i+arr[i:j].index(strreqd)+len(strreqd)
        except:
            return [-1,-1]
        return ans

#attemptt4&5:WA and TLE
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        nones=arr.count(1)
        if nones%3:
            return [-1,-1]
        nones=nones//3
        if nones==0:
            return [0,2]
        di={}
        count=0
        for i in range(len(arr)):
            if arr[i]:
                di[count+1]=i
                count+=1
            arr[i]=str(arr[i])
        i=di[nones]
        
        while(i<di[nones+1]):
            j=di[2*nones]+1
            flag=1
            while(flag or j<di[2*nones+1]):
                flag=0
                if "".join(arr[:i+1]).lstrip("0")=="".join(arr[i+1:j]).lstrip("0")=="".join(arr[j:]).lstrip("0"):
                    return [i,j]
                j+=1
            i+=1
        return [-1,-1]
        
'''

#attempt2&3: WA and TLE because seeing only till !=. HAs to be <
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        nones=arr.count(1)
        if nones%3:
            return [-1,-1]
        nones=nones//3
        if nones==0:
            return [0,2]
        di={}
        count=0
        for i in range(len(arr)):
            if arr[i]:
                di[count+1]=i
                count+=1
            arr[i]=str(arr[i])
        i=di[nones]
        
        while(i!=di[nones+1]):
            j=di[2*nones]+1
            while(j!=di[2*nones+1]):
                if "".join(arr[:i+1]).lstrip("0")=="".join(arr[i+1:j]).lstrip("0")=="".join(arr[j:]).lstrip("0"):
                    return [i,j]
                j+=1
            i+=1
        return [-1,-1]
'''

#attempt1: WA didnt think of that 0s could follow 1s in earlier subparts
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        nones=arr.count(1)
        if nones%3:
            return [-1,-1]
        nones=nones//3
        if nones==0:
            return [0,2]
        di={}
        count=0
        for i in range(len(arr)):
            if arr[i]:
                di[count+1]=i
                count+=1
            arr[i]=str(arr[i])
        i=di[nones]
        j=di[2*nones]+1
        if "".join(arr[:i+1]).lstrip('0')=="".join(arr[i+1:j]).lstrip('0')=="".join(arr[j:]).lstrip("0"):
            return [i,j]
        return [-1,-1]
'''
