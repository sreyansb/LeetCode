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
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.base_iterator = iterator
        self.nextval = -1
        self.hasnext = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.nextval == -1:
            self.hasnext = 1
            self.nextval = self.base_iterator.next()
        return self.nextval
        
        
    def next(self):
        """
        :rtype: int
        """
        temp = self.nextval
        if temp != -1:
            if self.base_iterator.hasNext():
                self.nextval = self.base_iterator.next()
            else:
                self.hasnext = 0
        else:
            temp = self.base_iterator.next()
            if self.base_iterator.hasNext():
                self.hasnext = 1
                self.nextval = self.base_iterator.next()
            else:
                self.hasnext = 0
        return temp
        

    def hasNext(self):
        return (self.hasnext or self.base_iterator.hasNext())==1
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
