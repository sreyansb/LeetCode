#attempt4: Sorted list and all
#reverse the array because adding to answer(i.e. appending becomes easier)
from sortedcontainers import SortedList        
from bisect import bisect_left
class Solution:
    def countSmaller(self, nums):
        n=len(nums)
        if sorted(nums)==nums:
            return [0]*n
        #print(nums)
        nums.reverse()
        ans=[0]
        final=SortedList([])
        final.add(nums[0])
        for i in nums[1:]:
            pos=final.bisect_left(i)
            ans.append(pos)
            final.add(i)
        #print(final)
        return ans[::-1]

#attempt3: TLE dont know why
'''
class bstnode:
    def __init__(self,val):
        self.val=val
        self.count=1
        self.right=None
        self.left=None
        self.leftcount=0
        self.rightcount=0
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if sorted(nums)==nums:
            return [0]*n
        #print(nums)
        nums.reverse()
        ans=[0]
        root=bstnode(nums[0])
        for i in nums[1:]:
            #print(i)
            rootc=root
            parent=None
            count=0
            while(rootc):
                parent=rootc
                if rootc.val<i:
                    rootc.rightcount+=1
                    count+=rootc.leftcount+rootc.count
                    rootc=rootc.right
                    
                elif rootc.val>i:
                    rootc.leftcount+=1
                    rootc=rootc.left
                
                else:
                    rootc.count+=1
                    break
            if rootc and rootc.val==i:
                count+=rootc.leftcount
                ans.append(count)
                continue
            if parent.val<i:
                parent.right=bstnode(i)
            else:
                parent.left=bstnode(i)
            ans.append(count)
        return ans[::-1]
'''

#attempt2:TLE - sorted ke liye seedha hi answer provide karo
'''
class bstnode:
    def __init__(self,val):
        self.val=val
        self.count=1
        self.right=None
        self.left=None
        self.leftcount=0
        self.rightcount=0
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums.reverse()
        #print(nums)
        ans=[0]
        root=bstnode(nums[0])
        for i in nums[1:]:
            rootc=root
            parent=None
            count=0
            while(rootc):
                parent=rootc
                if rootc.val<i:
                    rootc.rightcount+=1
                    count+=rootc.leftcount+rootc.count
                    rootc=rootc.right
                    
                elif rootc.val>i:
                    rootc.leftcount+=1
                    rootc=rootc.left
                
                else:
                    rootc.count+=1
                    break
            if rootc and rootc.val==i:
                count+=rootc.leftcount
                ans.append(count)
                continue
            if parent.val<i:
                parent.right=bstnode(i)
            else:
                parent.left=bstnode(i)
            ans.append(count)
        return ans[::-1]
'''

#attempt1: WA: Didnt think that if values are same then we have to add the left to it
#idea: make a bst with segment tree sort of structure and keep count of nodes lesser than and greater than a node at the node
'''
class bstnode:
    def __init__(self,val):
        self.val=val
        self.count=1
        self.right=None
        self.left=None
        self.leftcount=0
        self.rightcount=0
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums.reverse()
        ans=[0]
        root=bstnode(nums[0])
        for i in nums[1:]:
            rootc=root
            parent=None
            count=0
            while(rootc):
                parent=rootc
                if rootc.val<i:
                    rootc.rightcount+=1
                    count+=rootc.leftcount+rootc.count
                    rootc=rootc.right
                    
                elif rootc.val>i:
                    rootc.leftcount+=1
                    rootc=rootc.left
                
                else:
                    rootc.count+=1
                    break
            if rootc and rootc.val==i:
                ans.append(count)
                continue
            if parent.val<i:
                parent.right=bstnode(i)
            else:
                parent.left=bstnode(i)
            ans.append(count)
        return ans[::-1]
'''