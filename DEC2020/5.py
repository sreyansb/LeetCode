#attempt2: 72% and 30%
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        init=flowerbed.count(1)
        leng=len(flowerbed)
        if leng==1:
            if flowerbed[0]==0:
                return n==1 or n==0
            else:
                return n==0
        index=0
        while(index<leng):
            if n<=0:
                return True
            if index!=leng-1:
                if flowerbed[index]==0:
                    if flowerbed[index+1]==0:
                        n-=1
                        index+=2
                    else:
                        index+=3
                else:
                    index+=2
            elif index==leng-1:
                if flowerbed[index]==0:
                    if flowerbed[index-1]==0:
                        n-=1
                        index+=1
                    else:
                        index+=1
                else:
                    index+=1
        return n<=0
'''

#attempt1: 60%
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        init=flowerbed.count(1)
        leng=len(flowerbed)
        if leng==1:
            if flowerbed[0]==0:
                return n==1 or n==0
            else:
                return n==0
        def recurse(index,n):
            if index>=leng:
                return n<=0
            if n<=0:
                return True
            if index!=leng-1:
                if flowerbed[index]==0:
                    if flowerbed[index+1]==0:
                        return recurse(index+2,n-1)
                    else:
                        return recurse(index+3,n)
                else:
                    return recurse(index+2,n)
            elif index==leng-1:
                if flowerbed[index]==0:
                    if flowerbed[index-1]==0:
                        return recurse(index+1,n-1)
                    else:
                        return recurse(index+1,n)
                else:
                    return recurse(index+1,n)
        return recurse(0,n)
                        
            
                
            
                    
'''
