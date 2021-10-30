#attempt2: TOOK HINT
#the hint of binary searching the length is quite nice
#rabin karp not needed
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        def rabin_karp_at_index(s):
            d = 26
            #m=binary,searched
            l = []
            n = len(s)
            current = 0
            q = 29
            for i in range(n):
                current = (current*d + ord(s[i])-ord('a'))%q
                l.append(current)
            return l
        maxl = 0
        curw = ""
        endl = n-1
        startl = 0
        while(startl<=endl):
            midl = (startl+endl)//2
            flag=0
            di = set()
            for i in range(0,n-midl+1):
                word = s[i:i+midl]
                if word in di:
                    curw = word
                    flag=1
                    break
                di.add(word)
            if flag:
                startl = midl+1
            else:
                endl = midl - 1
        return curw

#attempt1: Didnt know what I was doing
# used some bisect stuff
'''
from bisect import bisect_right
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        dic = {}
        n = len(s)
        for index in range(n):
            i = s[index]
            if i not in dic:
                dic[i] = []
            dic[i].append(index)
        for i in dic:
            dic[i] = (dic[i],len(dic[i]))
        curstr = ""
        maxl = 0
        for index in range(n):
            ch = s[index]
            next_pos = bisect_right(dic[ch][0],index)
'''