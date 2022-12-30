#attempt2:
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexedTasks = [(index,task[0],task[1]) for index, task in enumerate(tasks)]
        indexedTasks.sort(key = lambda x: (x[1],x[2]))
        ans = []
        currentProcessing = []
        currentTime = 0
        taskHeap = []
        def consumeFromHeap(heap, currentTime):
            if heap:
                duration, index, start = heappop(heap)
                ans.append(index)
                startTime = max(currentTime,start)
                return [startTime, startTime + duration]
            return []
        for index,startTime,duration in indexedTasks:
            while currentProcessing and (currentProcessing[1] < startTime):
                currentTime = currentProcessing[1]
                currentProcessing = consumeFromHeap(taskHeap,currentTime)
            heappush(taskHeap, (duration,index,startTime))
            if not currentProcessing:
                currentProcessing = consumeFromHeap(taskHeap, currentTime)
        while(taskHeap):
            currentProcessing = consumeFromHeap(taskHeap, currentTime)
            currentTime = currentProcessing[1]
        return ans

#attempt1: 2nd event can be processed as soon as 1st event ends
'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        processingOrder = []
        for index,task in enumerate(tasks):
            heappush(processingOrder,(task[0],task[1],index))
        while(processingOrder):
            _,_,index = heappop(processingOrder)
            ans.append(index)
        return ans
'''
