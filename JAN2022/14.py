#attempt1:
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        fin = 0
        symbol = 1
        if not(s):
            return 0
        start = 0
        #print(s)
        if s[0] == "-":
            symbol = -1
            start = 1
        if s[0] == "+":
            start = 1
        for i in s[start:]:
            if i.isdigit():
                fin = fin*10 + (ord(i)-ord('0'))
            else:
                break
        fin *= symbol
        lim = (1<<31)
        if fin<-lim:
            fin = -lim
        elif fin>lim-1:
            fin = lim-1
        return fin
