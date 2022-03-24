#attempt2: 452ms
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people_len = len(people)
        actual_required = 0
        lastindex = people_len - 1
        firstindex = 0
        while(firstindex<=lastindex):
            if people[firstindex]+people[lastindex] <= limit:
                actual_required += 1
                firstindex += 1
                lastindex -= 1
            else:
                lastindex -= 1
                actual_required += 1
        return actual_required
                

#attempt1: 532 ms
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people_len = len(people)
        actual_required = people.count(limit)
        lastindex = people_len - actual_required - 1
        firstindex = 0
        while(firstindex<=lastindex):
            if people[firstindex]+people[lastindex] <= limit:
                actual_required += 1
                firstindex += 1
                lastindex -= 1
            else:
                lastindex -= 1
                actual_required += 1
        return actual_required
                
