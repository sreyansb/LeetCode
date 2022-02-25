#attempt2: AC
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        ans = 0
        v1 = v1.split(".")
        v2 = v2.split(".")
        v1len = len(v1)
        v2len = len(v2)
        reverse = 1
        if v1len<v2len:
            v1,v2 = v2,v1
            v1len,v2len = v2len,v1len
            reverse = -1
        for index in range(v1len):
            ele1 = int(v1[index])
            try:
                ele2 = int(v2[index])
            except:
                ele2 = 0
            if ele1>ele2:
                ans = 1
                break
            elif ele2>ele1:
                ans = -1
                break
        return ans*reverse

#attempt1: WA because didn't take into consideration reversal of v1 and v2
'''
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        ans = 0
        v1 = v1.split(".")
        v2 = v2.split(".")
        v1len = len(v1)
        v2len = len(v2)
        if v1len<v2len:
            v1,v2 = v2,v1
            v1len,v2len = v2len,v1len
        for index in range(v1len):
            ele1 = int(v1[index])
            try:
                ele2 = int(v2[index])
            except:
                ele2 = 0
            if ele1>ele2:
                ans = 1
                break
            elif ele2>ele1:
                ans = -1
                break
        return ans
            
                
        
'''
            
                
        
