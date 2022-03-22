#attempt4: Used binary Search : USE the variables carefully by understanding
#their meaning
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        final = ""
        '''
        while(n):
            for i in range(26):
                if k-(i+1)<=(n-1)*26:
                    final += chr(ord('a')+i)
                    k -= (i+1)
                    n -= 1
                    break
        return final
        '''
        i = 0
        while(i<26):
            left = 1
            right = n
            ans = -1 #represents the number of positions that can be filled
            while(left<=right):
                mid = (left+right)//2
                #print(left,right,mid,final)
                if (k-(i+1)*mid) <= (n-mid)*26:
                    ans = mid
                    left = mid+1
                else:
                    right = mid-1
            if ans != -1:
                n -= ans
                final += chr(ord('a')+i)*ans
                k -= ans*(i+1)
            i += 1
        
        return final
                        
        

#attempt3: TLE
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        final = ""
        i = 0
        while(n and i<26):
                for j in range(n,0,-1):
                    if k-j*(i+1) <= (n-j)*26:
                        n -= j
                        final += chr(ord('a')+i)*j
                        k -= j*(i+1)
                        break
                i += 1
        return final
'''

#attempt2: TLE 93/93 but still
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        final = ""
        
        for i in range(26):
                for j in range(n,0,-1):
                    if k-j*(i+1) <= (n-j)*26:
                        n -= j
                        final += chr(ord('a')+i)*j
                        k -= j*(i+1)
                        break
        return final
                        
        
'''

#attempt1: TLE 91/93
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        final = ""
        while(n):
            for i in range(26):
                if k-i-1<=(n-1)*26:
                    final += chr(ord('a')+i)
                    k -= (i+1)
                    n -= 1
                    break
        return final
'''
