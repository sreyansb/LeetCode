#aattempt1:
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        leftForces = [float('inf') for i in range(n)]
        rightForces = [float('inf') for i in range(n)]
        
        if dominoes[-1] == "L":
            leftForces[-1] = 0
        if dominoes[0] == "R":
            rightForces[0] = 0
        
        for index in range(n-2,-1,-1):
            if dominoes[index] == "R":
                leftForces[index] = float('inf')
            elif dominoes[index] == "L":
                leftForces[index] = 0
            else:
                leftForces[index] = leftForces[index+1]+1
        for index in range(1,n):
            if dominoes[index] == "R":
                rightForces[index] = 0
            elif dominoes[index] == "L":
                rightForces[index] = float('inf')
            else:
                rightForces[index] = rightForces[index-1]+1
        #print(leftForces,rightForces)
        ansString = ""
        for index in range(n):
            if dominoes[index] == ".":
                if leftForces[index] < rightForces[index]:
                    ansString += "L"
                elif leftForces[index] > rightForces[index]:
                    ansString += "R"
                else:
                    ansString += "."
            else:
                ansString += dominoes[index]
        return ansString
