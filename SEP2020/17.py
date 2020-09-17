#attempt 4: 65% and 97%
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction=0
        final=(0,0)
        for i in instructions:
            if i=='L':
                if direction==0:
                    direction=-1
                elif direction==-1:
                    direction=-2
                elif direction==-2:
                    direction=1
                elif direction==1:
                    direction=0
            elif i=='R':
                if direction==0:
                    direction=1
                elif direction==1:
                    direction=-2
                elif direction==-2:
                    direction=-1
                elif direction==-1:
                    direction=0
            else:
                if direction==0:
                    final=(final[0],final[1]+1)
                elif direction==-1:
                    final=(final[0]-1,final[1])
                elif direction==-2:
                    final=(final[0],final[1]-1)
                else:
                    final=(final[0]+1,final[1])
            #print(direction)
        return direction or final==(0,0)

#attempt3:AC
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        di={'G':0,'L':0,'R':0}
        for i in instructions:
            di[i]+=1
        if not(di['L'] or di['R']):
            return False
        direction=0
        final=(0,0)
        for i in instructions:
            if i=='L':
                if direction==0:
                    direction=-1
                elif direction==-1:
                    direction=-2
                elif direction==-2:
                    direction=1
                elif direction==1:
                    direction=0
            elif i=='R':
                if direction==0:
                    direction=1
                elif direction==1:
                    direction=-2
                elif direction==-2:
                    direction=-1
                elif direction==-1:
                    direction=0
            else:
                if direction==0:
                    final=(final[0],final[1]+1)
                elif direction==-1:
                    final=(final[0]-1,final[1])
                elif direction==-2:
                    final=(final[0],final[1]-1)
                else:
                    final=(final[0]+1,final[1])
        if direction or final==(0,0):
            return True
        return False
"""

#attempt2: took the clues WA 107/110
#used direction and final position but got wrong answer because I thought
#there wouldn't be any change in direction if count('L')==count('R')
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        di={'G':0,'L':0,'R':0}
        for i in instructions:
            di[i]+=1
        if not(di['L'] or di['R']) or di['L']==di['R']:
            return False
        direction=0
        final=(0,0)
        for i in instructions:
            if i=='L':
                if direction==0:
                    direction=-1
                elif direction==-1:
                    direction=-2
                elif direction==-2:
                    direction=1
                elif direction==1:
                    direction=0
            elif i=='R':
                if direction==0:
                    direction=1
                elif direction==1:
                    direction=-2
                elif direction==-2:
                    direction=-1
                elif direction==-1:
                    direction=0
            else:
                if direction==0:
                    final=(final[0],final[1]+1)
                elif direction==-1:
                    final=(final[0]-1,final[1])
                elif direction==-2:
                    final=(final[0],final[1]-1)
                else:
                    final=(final[0]+1,final[1])
        if direction or final==(0,0):
            return True
        return False
                    
                
        
"""

#attempt1 : had a faint idea WA 105/110. Thought that ONLY direction should change
#change of direction:I thought if both count('L')==count('R') no direction change. but wrong assumption
#WA for "GLGLGGLGL"
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        di={'G':0,'L':0,'R':0}
        for i in instructions:
            di[i]+=1
        if not(di['L'] or di['R']) or di['L']==di['R']:
            return False
        return True
"""
