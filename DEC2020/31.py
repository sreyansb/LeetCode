#attempt1: TO maintain order: like number of elements between current element and next minima on the right, use a **STACK**
#keep deleting from the stack as long as head element is bigger than current element(For elements coming after current element these deleted elements wont matter)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        elementstor=[]
        elementstol=[]
        stackr=[]
        stackl=[]
        for i in range(len(heights)-1,-1,-1):
            while(stackr and heights[stackr[-1]]>=heights[i]):
                stackr.pop()
            if not stackr:
                stackr.append(i)
                elementstor.append(len(heights)-i)
            else:
                elementstor.append(stackr[-1]-i)
                stackr.append(i)
        elementstor=elementstor[::-1]
        for i in range(0,len(heights)):
            while(stackl and heights[stackl[-1]]>=heights[i]):
                stackl.pop()
            if not stackl:
                stackl.append(i)
                elementstol.append(i+1)
            else:
                elementstol.append(i-stackl[-1])
                stackl.append(i)
        maxi=0
        for i in range(len(heights)):
            maxi=max(maxi,heights[i]*(elementstor[i]+elementstol[i]-1))
        return maxi
            
                
        
                    
        