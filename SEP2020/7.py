#Attempt 2: 94.27% and 50%
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        di={}
        dip={}
        str1=str.split()
        if len(pattern)!=len(str1) or len(set(pattern))!=len(set(str1)):
            return False
        else:
            flag=True
            i=0
            while(i<len(pattern)):
                if pattern[i] not in di:
                    if str1[i] not in dip:
                        di[pattern[i]]=str1[i]
                        dip[str1[i]]=pattern[i]
                    else:
                        flag=False
                        break
                else:
                    if di[pattern[i]]!=str1[i]:
                        flag=False
                        break
                
                i+=1
            return flag

#Attempt 1:82% and 1%
"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        di={}
        dip={}
        str1=str.split()
        if len(pattern)!=len(str1):
            return False
        else:
            flag=True
            i=0
            while(i<len(pattern)):
                if pattern[i] not in di:
                    if str1[i] not in dip:
                        di[pattern[i]]=str1[i]
                        dip[str1[i]]=pattern[i]
                    else:
                        flag=False
                        break
                else:
                    if di[pattern[i]]!=str1[i]:
                        flag=False
                        break
                
                i+=1
            return flag
"""
        
