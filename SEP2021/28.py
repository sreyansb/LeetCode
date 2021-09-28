#attempt2:
class Solution:
    def sortArrayByParityII(self, a: List[int]) -> List[int]:
        cureven=0
        curodd=1
        n=len(a)
        i=0
        while(i<n):
            if a[i]&1:
                if i&1:
                    i+=1
                else:
                    a[curodd],a[i]=a[i],a[curodd]
                    curodd+=2
            else:
                if i&1==0:
                    i+=1
                else:
                    a[cureven],a[i]=a[i],a[cureven]
                    cureven+=2
        return a
        

#attempt1:
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in nums:
            if i&1:
                odd.append(i)
            else:
                even.append(i)
        for i in range(0,len(nums),2):
            nums[i]=even.pop()
        for i in range(1,len(nums),2):
            nums[i]=odd.pop()
        return nums
'''