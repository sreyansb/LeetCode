#attempt1:
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskCounter = Counter(tasks)
        ans = -1
        if 1 not in taskCounter.values():
            ans = sum([ceil(taskCounter[task]/3) for task in taskCounter])
        return ans
