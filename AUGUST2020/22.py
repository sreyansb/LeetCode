from random import randint
from sys import maxsize
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects

    def pick(self) -> List[int]:
        selected=[]
        total=0
        for i in self.rects:
            area=(i[2]-i[0]+1)*(i[3]-i[1]+1)
            total+=area
            if randint(0,maxsize)%total<area:
                selected=i
        x=randint(0,maxsize)%(selected[2]-selected[0]+1)+selected[0]
        y=randint(0,maxsize)%(selected[3]-selected[1]+1)+selected[1]
        return [x,y]
