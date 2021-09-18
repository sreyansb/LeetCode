#attempt4: HACKED version using eval
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        ans=[]
        def curval(curstr):
            return eval(curstr)
        
        @lru_cache(None)
        def recurse(index,curstr):
            if index>=n:
                if curval(curstr)==target:
                    ans.append(curstr)
                return False
            if num[index]=="0":
                if curstr:
                    recurse(index+1,curstr+"+0") or recurse(index+1,curstr+"*0") or recurse(index+1,curstr+"-0")
                else:
                    recurse(index+1,curstr+"0") or recurse(index+1,curstr+"0") or recurse(index+1,curstr+"0")
                return
            for i in range(index+1,n+1):
                if curstr:
                    a=recurse(i,curstr+"+"+num[index:i]) or recurse(i,curstr+"*"+num[index:i]) or recurse(i,curstr+"-"+num[index:i])
                else:
                    a=recurse(i,curstr+num[index:i]) or recurse(i,curstr+num[index:i]) or recurse(i,curstr+num[index:i])
        recurse(0,"")
        return ans

#attempt3:
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        ans=set()
        
        @lru_cache(None)
        def recurse(index,curstr,curvalue,past):
            print(index,curvalue)
            if index>=n:
                if curvalue==target and ("+" in curstr or "-" in curstr or "*" in curstr):
                    ans.add(curstr)
                return
            for i in range(index+1,n+1):
                if curstr:
                    recurse(i,curstr+"+"+num[index:i],curvalue+int(num[index:i]),"-"+num[index:i])
                    recurse(i,curstr+"-"+num[index:i],curvalue-int(num[index:i]),"+"+num[index:i])
                    recurse(i,curstr+"*"+num[index:i],curvalue*int(num[index:i]),"/"+num[index:i])
                    if past[0]=="-":
                        recurse(i,curstr+"*"+num[index:i],((curvalue)-(int(past[1:])))+(int(past[1:])*int(num[index:i])),"/"+num[index:i])
                    elif past[0]=="+":
                        recurse(i,curstr+"*"+num[index:i],((curvalue)+(int(past[1:])))-(int(past[1:])*int(num[index:i])),"/"+num[index:i])
                else:
                    recurse(i,num[index:i],curvalue+int(num[index:i]),"-"+num[index:i])
                    recurse(i,num[index:i],curvalue-int(num[index:i]),"+"+num[index:i])       
        
        recurse(0,"",0,"+0")
        
        return list(ans)
'''

#attempt2: WA I dont know what I am doing
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        
        ans=[]
        
        @lru_cache(None)
        def recurse(index,curstr,curvalue,past):
            if index>=n:
                if curvalue==target:
                    ans.append(curstr)
                return
            for i in range(index+1,n+1):
                if curstr:
                    recurse(i+1,curstr+"+"+num[index:i],curvalue+int(num[index:i]),"-"+num[index:i])
                    recurse(i+1,curstr+"-"+num[index:i],curvalue-int(num[index:i]),"+"+num[index:i])
                    recurse(i+1,curstr+"*"+num[index:i],curvalue*int(num[index:i]),"/"+num[index:i])
                    if past[0]=='/':
                        recurse(i+1,curstr+"*"+num[index:i],((curvalue)/(int(past[1:])))*int(num[index:i]),"/"+num[index:i])
                    elif past[0]=="-":
                        recurse(i+1,curstr+"*"+num[index:i],((curvalue)-(int(past[1:])))*int(num[index:i]),"/"+num[index:i])
                    else:
                        recurse(i+1,curstr+"*"+num[index:i],((curvalue)+(int(past[1:])))*int(num[index:i]),"/"+num[index:i])
                else:
                    recurse(i+1,num[index:i],curvalue*int(num[index:i]),"/"+num[index:i])
                    recurse(i+1,num[index:i],curvalue+int(num[index:i]),"-"+num[index:i])
                    recurse(i+1,num[index:i],curvalue-int(num[index:i]),"+"+num[index:i])       
        recurse(0,"",0,"+0")
        return ans
'''

#attempt1:Terrible attempt: had a stack calculator which was wrong because of 
# precedence of * operaator
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        ans=[]
        
        @lru_cache(None)
        def recurse(index,curstr):
            if index>=n:
                if curval(curstr)==target:
                    ans.append(curstr)
                return False
            return recurse(index+1,curstr+"+"+num[index]) or recurse(index+1,curstr+"*"+num[index]) or recurse(index+1,curstr+"-"+num[index])
        
        recurse(1,num[0])
        return ans
"""