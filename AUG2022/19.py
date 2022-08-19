#attempt3:
from heapq import heapify,heappop
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = list(set(nums))
        heapify(heap)
        di = Counter(nums)
        def check(ele):
            return ele+1 in di and di[ele+1]>=di[ele] and ele+2 in di and di[ele+2]>=di[ele]
        di_each_list = {} #highest element with its occurence
        while(heap):
            min_ele = heappop(heap)
            #print(min_ele,di_each_list,di)
            if di[min_ele] == 0:
                continue
            min_ele_count = di[min_ele]
            if min_ele-1 in di_each_list and di_each_list[min_ele-1]>0:
                if di[min_ele] <= di_each_list[min_ele-1]:
                    if min_ele not in di_each_list:
                        di_each_list[min_ele] = 0
                    di_each_list[min_ele] += di[min_ele]
                    di_each_list[min_ele-1] -= di[min_ele]
                else:
                    di[min_ele] -= di_each_list[min_ele-1]
                    if min_ele not in di_each_list:
                        di_each_list[min_ele] = 0
                    di_each_list[min_ele] += di_each_list[min_ele-1]
                    di_each_list[min_ele-1] = 0
                    heappush(heap,min_ele)
                continue
            if check(min_ele):
                if min_ele+2 not in di_each_list:
                    di_each_list[min_ele+2] = 0
                di_each_list[min_ele+2] += di[min_ele]
                di[min_ele+1] -= di[min_ele]
                di[min_ele+2] -= di[min_ele]
                di[min_ele] = 0
            else:
                #print(min_ele,di_each_list)
                return False
            
        return True
                    
            
            

#attempt2: WA because values can be added
'''
from heapq import heapify,heappop
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = list(set(nums))
        heapify(heap)
        di = Counter(nums)
        def check(ele):
            return ele+1 in di and di[ele+1]>=di[ele] and ele+2 in di and di[ele+2]>=di[ele]
        di_each_list = {} #highest element with its occurence
        while(heap):
            min_ele = heappop(heap)
            if di[min_ele] == 0:
                continue
            min_ele_count = di[min_ele]
            if min_ele-1 in di_each_list and di_each_list[min_ele-1]>0:
                if di[min_ele] <= di_each_list[min_ele-1]:
                    di_each_list[min_ele] = di[min_ele]
                    di_each_list[min_ele-1] -= di[min_ele]
                else:
                    di[min_ele] -= di_each_list[min_ele-1]
                    di_each_list[min_ele] = di_each_list[min_ele-1]
                    di_each_list[min_ele-1] = 0
                    heappush(heap,min_ele)
                continue
            if check(min_ele):
                if min_ele+2 not in di_each_list:
                    di_each_list[min_ele+2] = 0
                di_each_list[min_ele+2] += di[min_ele]
                di[min_ele+1] -= di[min_ele]
                di[min_ele+2] -= di[min_ele]
                di[min_ele] = 0
            else:
                return False
            
        return True
'''

#attempt1: WA because we have to append to an existing sequence before
#making a new sequence
'''
from heapq import heapify,heappop
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = list(set(nums))
        heapify(heap)
        di = Counter(nums)
        def check(ele):
            return ele+1 in di and di[ele+1]>=di[ele] and ele+2 in di and di[ele+2]>=di[ele]
        di_each_list = {} #highest element with its occurence
        while(heap):
            min_ele = heappop(heap)
            if di[min_ele] == 0:
                continue
            min_ele_count = di[min_ele]
            if check(min_ele):
                if min_ele+2 not in di_each_list:
                    di_each_list[min_ele+2] = 0
                di_each_list[min_ele+2] += di[min_ele]
                di[min_ele+1] -= di[min_ele]
                di[min_ele+2] -= di[min_ele]
                di[min_ele] = 0
            else:
                if min_ele-1 in di_each_list:
                    if di_each_list[min_ele-1] < di[min_ele]:
                        return False
                    else:
                        di_each_list[min_ele-1] -= di[min_ele]
                        di_each_list[min_ele] = di[min_ele]
                else:
                    return False
        return True
'''
