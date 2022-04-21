#attempt2: set.remove gives run time error if element not present
class MyHashSet:

    def __init__(self):
        self.elements = set()
        

    def add(self, key: int) -> None:
        self.elements.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.elements:
            self.elements.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.elements
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
