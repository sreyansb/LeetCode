#attempt1:
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        if start == end:
            return 0
        
        def findDifference(firstMutation, secondMutation):
            count = 0
            for index in range(len(firstMutation)):
                count += firstMutation[index] != secondMutation[index]
            return count                
        
        def bfs():
            visited = set()
            queue = deque([(start,0)])
            visited.add(start)
            while(queue):
                curWord,steps = queue.popleft()
                if curWord == end:
                    return steps
                for mutation in bank:
                    if mutation not in visited and findDifference(curWord,mutation) == 1:
                        visited.add(mutation)
                        queue.append((mutation,steps+1))
            return -1
        
        return bfs()
