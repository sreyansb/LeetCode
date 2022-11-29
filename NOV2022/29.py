#attempt1:
from random import choice
class RandomizedSet:

    def __init__(self):
        self.elementSet = set()

    def insert(self, val: int) -> bool:
        ans = False
        if val not in self.elementSet:
            ans = True
        self.elementSet.add(val)
        return ans

    def remove(self, val: int) -> bool:
        if val not in self.elementSet:
            return False
        self.elementSet.remove(val)
        return True

    def getRandom(self) -> int:
        return choice(tuple(self.elementSet))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
