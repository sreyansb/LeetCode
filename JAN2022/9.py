#attempt1: TOOK HINTS, no idea how to solve
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curpos = [0,0]
        curdir = 0#0 is for North,1 is for South,2 is for east,3 is for West
        for i in instructions:
            if i == "G":
                if curdir == 0:
                    curpos[1] += 1
                elif curdir == 1:
                    curpos[1] -= 1
                elif curdir == 2:
                    curpos[0] += 1
                else:
                    curpos[0] -= 1
            elif i == "L":
                if curdir == 0:
                    curdir = 3
                elif curdir == 1:
                    curdir = 2
                elif curdir == 2:
                    curdir = 0
                else:
                    curdir = 1
            else:
                if curdir == 0:
                    curdir = 2
                elif curdir == 1:
                    curdir = 3
                elif curdir == 2:
                    curdir = 1
                else:
                    curdir = 0
        return curpos == [0,0] or curdir!=0
        
        
        
        
