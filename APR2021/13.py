#attempt2:
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

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def check(li):
            ans=[]
            for i in li:
                if i.isInteger():
                    ans.append(i.getInteger())
                else:
                    ans+=check(i.getList())
            return ans
        self.li=[]
        for i in nestedList:
            if i.isInteger():
                self.li.append(i.getInteger())
            else:
                self.li+=check(i.getList())
        self.n=0
        self.leng=len(self.li)
    def next(self) -> int:
        self.n+=1
        return self.li[self.n-1]       
    
    def hasNext(self) -> bool:
         return self.n<self.leng

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#attmept1: WA because type(i) is not the right thing to do.
#objects are of type NestedInteger and not int as is
'''
class NestedIterator:
    def __init__(self, nestedList):
        def check(li):
            ans=[]
            for i in li:
                if type(i)==list:
                    ans+=check(i)
                else:
                    ans.append(i)
            return ans
        self.li=[]
        for i in nestedList:
            if type(i)==list:
                self.li+=check(i)
            else:
                self.li.append(i) 
        self.n=0
        self.leng=len(self.li)
    def next(self):
        self.n+=1
        return self.li[self.n-1]

    
    def hasNext(self):
         return self.n<self.leng
nestedList=([1,[4,[6]]])
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
print(v)
'''
