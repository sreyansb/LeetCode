#3rd  attempt
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num>0:
            return not(num&(num-1)) and len(bin(num))&1
        return False
"""
#2nd attempt
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num>0:
            i=1
            po=2
            while(i!=num and po<=32):
                i=1<<po
                po+=2
            return i==num
        else:
            return False
"""
"""
#1st attempt
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num>0:
            s=bin(num)[2:]
            if s.count('1')==1 and s.count('0')&1==0:
                return True
            return False
        else:
            return False
"""          
        
