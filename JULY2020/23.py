#3rd attempt->Clues
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=0
        for i in nums:
            a^=i
        j=a&-a
        ans=0
        for i in nums:
            if j&i:
                ans^=i
        return [ans,a^ans]


"""
#2nd attempt->faster but many violations of requirements
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        nums.sort()
        for i in nums:
            if l and l[-1]==i:
                l.pop()
            else:
                l.append(i)
        return l
"""            
        

"""
#1st attempt->very slow
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        di={}
        for i in nums:
            if i not in di:
                di[i]=0
            di[i]+=1
        l=[]
        for i in di:
            if di[i]==1:
                l.append(i)
        return l
"""

        
