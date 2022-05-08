#attempt1:
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

def openList(nestedList):
    if nestedList.isInteger():
        return [nestedList.getInteger()]
    ans = []
    for nextList in nestedList.getList():
        ans = ans + openList(nextList)
    return ans
        

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.finlist = []
        for nestedlist in nestedList:
            self.finlist += openList(nestedlist)
        self.index = 0
        self.len = len(self.finlist)
    
    def next(self) -> int:
        self.index += 1
        return self.finlist[self.index-1]
        
    
    def hasNext(self) -> bool:
         return self.index < self.len

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
