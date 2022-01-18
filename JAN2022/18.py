#attempt2:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arrlen = len(flowerbed)
        disttonext = [float('inf') for i in range(arrlen)]
        if flowerbed[0]:
            disttonext[0] = 0
        for i in range(1,arrlen):
            if flowerbed[i] == 0:
                disttonext[i] = disttonext[i-1] + 1
            else:
                disttonext[i] = 0
        for i in range(arrlen-2,-1,-1):
            if flowerbed[i] == 0:
                disttonext[i] = min(disttonext[i+1] + 1,disttonext[i])
        for i in range(arrlen):
            if n==0:
                break
            if i>0:
                disttonext[i] = min(disttonext[i-1]+1,disttonext[i])
            if disttonext[i] >= 2:
                n -= 1
                disttonext[i] = 0
        return n==0

#aattempt1: WA
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arrlen = len(flowerbed)
        disttonext = [0 for i in range(arrlen)]
        for i in range(1,arrlen):
            if flowerbed[i] == 0:
                disttonext[i] = disttonext[i-1] + 1
        for i in range(arrlen-2,-1,-1):
            if flowerbed[i] == 0:
                disttonext[i] = min(disttonext[i+1] + 1,disttonext[i])
        for i in range(arrlen):
            if n==0:
                break
            if i>0:
                disttonext[i] = min(disttonext[i-1]+1,disttonext[i])
            if disttonext[i] >= 2:
                n -= 1
                disttonext[i] = 0
        return n==0
'''
