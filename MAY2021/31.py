#attempt1: TOOK HINT great problem not every pattern matching part is TRIE
from bisect import bisect_right
class Solution:
    def suggestedProducts(self, products: List[str], searchword: str) -> List[List[str]]:
        products.sort()
        ans=[]
        for i in range(1,len(searchword)+1):
            allowed=[j for j in products if j.startswith(searchword[:i])]
            if not(allowed):
                ans.append([])
                continue
            ans.append(allowed[:min(len(allowed),3)])
        return ans
            
            
            