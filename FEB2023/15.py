#attempt1:
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = int("".join([str(i) for i in num]))
        s = str(number+k)
        return [int(i) for i in s]
