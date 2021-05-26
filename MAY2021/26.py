#attempt1: Seems very difficult
#but is simple in the fact that we need atleast as many 1s as required in max number
#we can tweak other positions to have 0 to support our hypothesis
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
        