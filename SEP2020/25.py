#attempt8: Accepted-95% - Had to take help basically sort based on concatenated strings
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        di={}
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            if nums[i][0] not in di:
                di[nums[i][0]]=[]
            di[nums[i][0]].append(nums[i])
        mainans=""
        for i in sorted(di.keys(),reverse=True):
            for k in range(len(di[i])-1):
                l=k
                for j in range(l+1,len(di[i])):
                    if di[i][j]+di[i][l]>=di[i][l]+di[i][j]:
                        l=j
                di[i][l],di[i][k]=di[i][k],di[i][l]
            #print(i,di[i])
            mainans+="".join(di[i]) 
        mainans=str(int(mainans))
        return mainans

#attempt7:WA 218/222
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        di={}
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            if nums[i][0] not in di:
                di[nums[i][0]]=[]
            di[nums[i][0]].append(nums[i])
        mainans=""
        for i in sorted(di.keys(),reverse=True):
            for k in range(len(di[i])-1):
                l=k
                for j in range(l+1,len(di[i])):
                    if di[i][j]+di[i][l]>=di[i][l]+di[i][j]:
                        l=j
                di[i][l],di[i][k]=di[i][k],di[i][l]
            #print(i,di[i])
            mainans+="".join(di[i]) 
        mainans.strip("0")
        return mainans
"""

#attempt6:WA 160/222
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        di={}
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            if nums[i][0] not in di:
                di[nums[i][0]]=[]
            di[nums[i][0]].append(nums[i])
        mainans=""
        for i in sorted(di.keys(),reverse=True):
            for k in range(len(di[i])-1):
                l=k
                for j in range(l+1,len(di[i])):
                    w1=di[i][l]
                    w2=di[i][j]
                    minl=min(len(w1),len(w2))-1
                    if len(w1)>len(w2):
                        w2=w2+"0"*(len(w1)-len(w2))
                    else:
                        w1=w1+"0"*(len(w2)-len(w1))
                    if int(w2)>=int(w1) or w2[minl]>w1[minl]:
                        l=j
                di[i][k],di[i][l]=di[i][l],di[i][k]
            #print(i,di[i])
            mainans+="".join(di[i])
        return mainans
"""

#attempt3: 188/222
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        di={}
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            if nums[i][0] not in di:
                di[nums[i][0]]=[]
            di[nums[i][0]].append(nums[i])
        mainans=""
        for i in sorted(di.keys(),reverse=True):
            for k in range(len(di[i])-1):
                l=k
                for j in range(l+1,len(di[i])):
                    w1=di[i][l]
                    w2=di[i][j]
                    if len(w1)>len(w2):
                        w2=w2+"0"*(len(w1)-len(w2))
                    else:
                        w1=w1+"0"*(len(w2)-len(w1))
                    if int(w2)>int(w1):
                        l=j
                di[i][k],di[i][l]=di[i][l],di[i][k]
            #print(i,di[i])
            mainans+="".join(di[i])
        return mainans
"""

#attempt2: 126/222
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        di={}
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            if nums[i][0] not in di:
                di[nums[i][0]]=[]
            di[nums[i][0]].append(nums[i])
        mainans=""
        for i in sorted(di.keys(),reverse=True):
            prefix=""
            suffix=""
            di[i].sort(key=lambda x:x[-1],reverse=True)
            for j in di[i]:
                if j[-1]<=i:
                    suffix+=j+suffix
                else:
                    prefix+=j
            mainans+=prefix+suffix
        return mainans
"""

#attempt1: WA 180/222 cases because for"30","3" we can have 330 and not 303
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(reverse=True)
        return "".join(nums)
"""
