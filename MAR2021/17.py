#attempt3: TOOK HELP, POLAR coordinates but why do we need to have
#random()**0.5 for random radius?
from random import random
from math import sin,cos,pi

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius=radius
        self.x=x_center
        self.y=y_center

    def randPoint(self) -> List[float]:
        angle=2*pi*random()
        leng=(random())**0.5*self.radius
        x=self.x+leng*cos(angle)
        y=self.y+leng*sin(angle)
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

#attempt2:WA - Dont know why, probably distribution
'''
from random import uniform,choice
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius=radius
        self.x=x_center
        self.y=y_center

    def randPoint(self) -> List[float]:
        x=uniform(self.x+self.radius,self.x-self.radius)
        y=uniform(self.y+self.radius,self.y-self.radius)
        if x*x+y*y>self.radius*self.radius:
            return self.randPoint()
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
'''

#attempt1: multiple WAs-read the statement properly, they are asking about points within
#a circle and not on boundary
'''
from random import uniform,choice
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius=radius
        self.x=x_center
        self.y=y_center

    def randPoint(self) -> List[float]:
        x=uniform(self.x+self.radius,self.x-self.radius)
        y=self.y+choice([1,-1])*(2*x*self.x+self.radius*self.radius-x*x-self.x*self.x)**0.5
        #print(x*x+y*y==self.radius*self.radius)
        if type(y)==complex:
            return self.randPoint()
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
'''
