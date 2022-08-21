#attempt2:
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamps = {stamp}
        n = len(stamp)
        for index in range(n):
            for index2 in range(index+1,n+1):
                stamps.add("?"*index+stamp[index:index2]+"?"*(n-index2))
        #stamps.remove("?"*n)
        ans = []
        #print(stamps)
        target = list(target)
        while(target != ["?"]*len(target)):
            #print(target)
            flag = 0
            for index in range(len(target)-n+1):
                if "".join(target[index:index+n]) in stamps:
                    flag = 1
                    ans.append(index)
                    target[index:index+n] = ["?"]*n
                    break
            if not(flag):
                return []
        #print(ans)
        return ans[::-1] if len(ans) <=10*len(target) else []
        

#attempt1: bcoz I didnt take care of this masking : abc -> ?b?
'''
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamps = {stamp}
        n = len(stamp)
        for index in range(n):
            stamps.add(stamp[:index]+"?"*(n-index))
        s = stamp[::-1]
        for index in range(n):
            stamps.add((s[:index]+"?"*(n-index))[::-1])
        stamps.remove("?"*n)
        ans = []
        #print(stamps)
        target = list(target)
        while(target != ["?"]*len(target)):
            flag = 0
            for index in range(len(target)-n+1):
                if "".join(target[index:index+n]) in stamps:
                    flag = 1
                    ans.append(index)
                    target[index:index+n] = ["?"]*n
                    break
            if not(flag):
                return []
        return ans[::-1] if len(ans) <=10*len(target) else []
'''
