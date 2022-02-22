#attempt3: Best
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = 0
        k = ord('A')-1
        for i in columnTitle:
            col = col*26 + ord(i)-k
        return col
        

#aattempt2: 24ms
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = 0
        #k = ord('A')-1
        for i in columnTitle:
            col = col*26 + 64
        return col
        

#attempt1: 76 ms
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = 0
        for i in columnTitle:
            col = col*26 + ord(i)-ord('A')+1
        return col
        
