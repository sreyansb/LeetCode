#atttempt2:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        @lru_cache(None)
        def findAns(currentIndex,partitionsDone):
            if currentIndex >= n:
                if partitionsDone != 4:
                    return ["invalid"]
                return [""]
            if partitionsDone == 4:
                return ["invalid"]
            highestIndexToGoTo = 3
            if s[currentIndex] == "0":
                highestIndexToGoTo = 1
            ans = []
            for groupedIndex in range(currentIndex,min(currentIndex+highestIndexToGoTo,n)):
                number = s[currentIndex:groupedIndex+1]
                if int(number) > 255:
                    continue
                nextList = findAns(groupedIndex+1,partitionsDone+1)
                if nextList != ["invalid"]:
                    for nextAns in nextList:
                        ans.append((number+"."+nextAns).strip("."))
            return ans
        
        return findAns(0,0)

#attempt1:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        @lru_cache(None)
        def findAns(currentIndex,partitionsDone):
            if currentIndex >= n:
                if partitionsDone != 4:
                    return False
                return [""]
            if partitionsDone == 4:
                return False
            highestIndexToGoTo = 3
            if s[currentIndex] == "0":
                highestIndexToGoTo = 1
            ans = []
            for groupedIndex in range(currentIndex,min(currentIndex+highestIndexToGoTo,n)):
                number = s[currentIndex:groupedIndex+1]
                if int(number) > 255:
                    continue
                nextList = findAns(groupedIndex+1,partitionsDone+1)
                if nextList != False:
                    for nextAns in nextList:
                        ans.append((number+"."+nextAns).strip("."))
            return ans
        
        return findAns(0,0)
