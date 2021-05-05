#attempt1:
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        fin=[first]
        for i in encoded:
            fin.append(fin[-1]^i)
        return fin
        
