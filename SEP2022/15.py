#attempt2:
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n&1:
            return []
        counts = Counter(changed)
        di = {}
        counts_having = 0
        ans = []
        changed.sort()
        for change in changed:
            if change not in counts:
                continue
            counts[change] -= 1
            if counts[change] == 0:
                del counts[change]
            change_double = change*2
            if change_double in counts:
                counts_having += 1
                ans.append(change)
                counts[change_double] -= 1
                if counts[change_double] == 0:
                    del counts[change_double]
        if counts_having == n//2:
            return ans
        return []

#attempt1: PoC was wrong because 1->2, 3->6, 4->8 for [1,2,3,4,6,8]
'''
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n&1:
            return []
        di = Counter(changed)
        changed.sort()
        for element in changed[:n//2]:
            if di[element] == 0:
                return []
            if element*2 not in di or di[element*2] == 0:
                return []
            di[element*2] -= 1
        return changed[:n//2]
'''
