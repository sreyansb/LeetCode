#attempt3: VERY IMPORTANT ONLY MATH
class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        steps,k=0,0
        while(steps<target):
            k+=1
            steps+=k
        while((steps-target)&1):
            k+=1
            steps+=k
        return k

#attempt2:TLE
'''
from collections import deque
class Solution:
    def reachNumber(self, target: int) -> int:
        if target==0:
            return 0
        queue=deque()
        queue.append((0,0,1))
        while(queue):
            #print(queue)
            curi,steps,nexts=queue.popleft()
            if curi==target:
                return steps
            if curi+nexts==target:
                return nexts
            if curi-nexts==target:
                return nexts
            queue.append((curi+nexts,nexts,nexts+1))
            queue.append((curi-nexts,nexts,nexts+1))
'''


#attempt1:WA
'''
class Solution:
    def reachNumber(self, target: int) -> int:
        if target==0:
            return 0
        steps=1
        start=0
        while(start!=target):
            if start+steps<=target:
                start+=steps
            else:
                start-=steps
            steps+=1
        return steps
'''