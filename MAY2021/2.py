#attempt4:TOOK HELP
#max heap for durations (taken now) is implemented
#push current element to heap, check if the deadline condition is satisfied
#till now, if not remove top most element from the heap.
#DOUBT CLARIFICATION: at a certain point where the above condition of deadline
#isn't satisfied and heap part removal of duration
#

from heapq import heappush,heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses=[i for i in courses if i[0]<=i[1]]
        if not courses:
            return 0
        courses.sort(key=lambda x:(x[1]))
        heap=[]
        curt=0
        for i in courses:
            heappush(heap,-i[0])
            curt+=i[0]
            if curt>i[1]:
                curt+=heappop(heap)
        return len(heap)
                

#attempt3: TOOK HELP WA Did heaps part: 
#because the current element's duration needs to pushed to heap first
#only then do we check it
'''
from heapq import heappush,heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses=[i for i in courses if i[0]<=i[1]]
        if not courses:
            return 0
        heap=[]
        curt=0
        for i in courses:
            heappush(heap,-i[0])
            curt+=i[0]
            if curt>i[1]:
                curt+=heappop(heap)
        return len(heap)
'''

#attempt2: Need to use heaps
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses=[i for i in courses if i[0]<=i[1]]
        if not courses:
            return 0
        courses.sort(key=lambda x:(x[0],x[1]))
        noc=1
        curday=courses[0][0]
        for i in courses[1:]:
            if curday+i[0]<=i[1]:
                curday+=i[0]
                noc+=1
        return noc
'''

#attempt1:WA WE need to sort based on deadline
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses=[i for i in courses if i[0]<=i[1]]
        if not courses:
            return 0
        courses.sort(key=lambda x:(x[1],x[0]))
        noc=1
        prev=courses[0]
        for i in courses[1:]:
            if i[0]>=prev[1]:
                noc+=1
                prev=i
        return noc
'''
