#attempt1: TOOK HELP
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        heap = []
        totalhourstillnow = 0
        coursetillnow = 0
        for course in courses:
            heappush(heap,-course[0])
            totalhourstillnow += course[0]
            if totalhourstillnow > course[1]:
                totalhourstillnow += heappop(heap)
        return len(heap)
        
