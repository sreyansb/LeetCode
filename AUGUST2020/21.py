#2nd attempt:
#fast only but better memory management
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x:x%2)
        return A
"""
#1st attempt-> very fast but terrible memory management
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in A:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        return even+odd
"""        

