#attempt4: WA: can't use float to check if the number is valid
'''
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n=len(s)
        def findstr(s):
            if not(s):
                return []
            if s[0]=="0":
                if s=="0":
                    return ["0"]
                if set(s)=={"0"}:
                    return []
                else:
                    if str(float("0."+s[1:]))=="0."+s[1:]:
                        return ["0."+s[1:]]
            else:
                arr=[s]
                if s[-1]=="0":
                    return arr
                for i in range(1,len(s)):
                    if set(s[i:])=={"0"}:
                        continue
                    if str(float(s[:i]+"."+s[i:]))==s[:i]+"."+s[i:]:
                        arr.append(s[:i]+"."+s[i:])
                return arr
        ans=set()
        s=s[1:-1]
        n-=2
        for i in range(n-1):
            a1,a2=findstr(s[:i+1]),findstr(s[i+1:])
            if not(a1) or not(a2):
                continue
            for i in a1:
                for j in a2:
                    ans.add("("+i+", "+j+")")   
        return list(ans)
'''

#attempt3: AC
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n=len(s)
        def findstr(s):
            if not(s):
                return []
            if s[0]=="0":
                if s=="0":
                    return ["0"]
                if set(s)=={"0"}:
                    return []
                else:
                    if s[-1]=="0":
                        return []
                    return ["0."+s[1:]]
            else:
                arr=[s]
                if s[-1]=="0":
                    return arr
                for i in range(1,len(s)):
                    if set(s[i:])=={"0"}:
                        continue
                    arr.append(s[:i]+"."+s[i:])
                return arr
        ans=set()
        s=s[1:-1]
        for i in range(n-2):
            a1,a2=findstr(s[:i+1]),findstr(s[i+1:])
            if not(a1) or not(a2):
                continue
            for i in a1:
                for j in a2:
                    ans.add("("+i+", "+j+")")   
        return list(ans)

#attempt2: WA because I didnt care about trailing zeroes in decimal part of the
#number
'''
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n=len(s)
        def findstr(s):
            if not(s):
                return []
            if s[0]=="0":
                if s=="0":
                    return ["0"]
                if set(s)=={"0"}:
                    return []
                else:
                    return ["0."+s[1:]]
            else:
                arr=[s]
                for i in range(1,len(s)):
                    if set(s[i:])=={"0"}:
                        continue
                    arr.append(s[:i]+"."+s[i:])
                return arr
        ans=set()
        s=s[1:-1]
        for i in range(n-2):
            a1,a2=findstr(s[:i+1]),findstr(s[i+1:])
            if not(a1) or not(a2):
                continue
            for i in a1:
                for j in a2:
                    ans.add("("+i+", "+j+")")   
        return list(ans)           
'''


#attempt1: WA see the correct output: there was space between abscissa and oridinate
'''
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n=len(s)
        def findstr(s):
            if not(s):
                return []
            if s[0]=="0":
                if s=="0":
                    return ["0"]
                if set(s)=={"0"}:
                    return []
                else:
                    return ["0."+s[1:]]
            else:
                arr=[s]
                for i in range(1,len(s)):
                    if set(s[i:])=={"0"}:
                        continue
                    arr.append(s[:i]+"."+s[i:])
                return arr
        ans=set()
        s=s[1:-1]
        for i in range(n-2):
            a1,a2=findstr(s[:i+1]),findstr(s[i+1:])
            if not(a1) or not(a2):
                continue
            for i in a1:
                for j in a2:
                    ans.add("("+i+","+j+")")   
        return list(ans)        
'''
