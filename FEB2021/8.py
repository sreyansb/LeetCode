#attempt1:
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.leng=0
        self.arr=[]
        while(iterator.hasNext()):
            self.arr.append(iterator.next())
            self.leng+=1
        #print(self.arr)
        self.index=0        

    def peek(self):
        if self.index<self.leng:
            return self.arr[self.index]        

    def next(self):
        if self.hasNext():
            self.index+=1
            return self.arr[self.index-1]
            
        

    def hasNext(self):
        return self.index<self.leng
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
