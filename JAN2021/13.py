#attempt1: I was overthinking regarding two dictionaries and all.
#it was a simple approach: sort and use 2 pointers
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nob=0
        people.sort()
        start=0
        end=len(people)-1
        while(start<=end):
            if people[start]+people[end]<=limit:
                start+=1
            end-=1
            nob+=1
        return nob
