#attempt1:
from math import log2
class Solution:
    def findComplement(self, num: int) -> int:
        dig_req = int(log2(num))+1
        newnumber = int("1"*dig_req,2)
        #print(newnumber)
        return num^newnumber
        
        
        
