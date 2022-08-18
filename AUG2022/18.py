#attempt2:
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        di = Counter(arr)
        n = len(arr)
        removed = 0
        index = 0
        di_keys = sorted(di.keys(),key = lambda x:-di[x])
        while(removed<n//2):
            removed += di[di_keys[index]]
            index += 1
        return index

#attempt1: WA because I was removing the number and not the values
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        di = Counter(arr)
        n = len(arr)
        removed = 0
        index = 0
        di_keys = sorted(di.keys(),key = lambda x:-di[x])
        while(removed<n//2):
            removed += di[di_keys[index]]
            index += 1
        return index
'''
