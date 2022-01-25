#attempt2: WA: what if the array is sorted
'''
class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        downs = 0
        ups = 1
        n = len(a)
        if n < 3:
            return False
        if not(a[0]<a[1]):
            return False
        for i in range(1,n):
            if a[i]>a[i-1]:
                if ups == 0:
                    return False
            elif a[i]<a[i-1]:
                if ups == 1:
                    if downs == 0:
                        ups = 0
                        downs = 1
                    else:
                        return False
                else:
                    if downs == 0:
                        return False
            else:
                return False
        return True
'''

#attempt1: 302ms
class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        downs = 0
        ups = 1
        n = len(a)
        if n < 3:
            return False
        if not(a[0]<a[1]):
            return False
        for i in range(1,n):
            if a[i]>a[i-1]:
                if ups == 0:
                    return False
            elif a[i]<a[i-1]:
                if ups == 1:
                    if downs == 0:
                        ups = 0
                        downs = 1
                    else:
                        return False
                else:
                    if downs == 0:
                        return False
            else:
                return False
        return ups==0 and downs==1
