#attempt2:
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans=set()
        if bound<2:
            return []
        if x==y==1:
            return [2]
        if x==1:
            x,y=y,x
        limx=0
        while(x**limx<=bound):
            limx+=1
        for i in range(limx):
            j=0
            if y==1 and (x**i)+1<=bound:
                ans.add((x**i)+1)
            else:
                while(x**i+y**j<=bound):
                    ans.add((x**i)+(y**j))
                    j+=1
        return list(ans)        

#attempt1: TLE because didn't take care of x or y == 1
'''
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans=set()
        if bound<2:
            return []
        limx=0
        while(x**limx<=bound):
            limx+=1
        for i in range(limx):
            j=0
            while(x**i+y**j<=bound):
                ans.add((x**i)+(y**j))
                j+=1
        return list(ans)
'''
