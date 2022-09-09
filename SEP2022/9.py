#attempt3:
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(-x[0],x[1]))
        maxDefense = 0
        ans = 0
        for property in properties:
            if property[1] < maxDefense:
                ans += 1
            else:
                maxDefense = property[1]
        return ans
        
        
                

#attempt2: TLE
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:x[0])
        n = len(properties)
        ans = 0
        print(properties)
        for index in range(n):
            for index2 in range(index+1,n):
                if properties[index][0]<properties[index2][0] and properties[index][1]<properties[index2][1]:
                    ans += 1
                    break
        return ans
                
'''

#attempt1: WA
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:-x[0])
        onlyDefense = []
        prev = -1
        min_prev = 0
        n = len(properties)
        ans = 0
        for index in range(n):
            for index2 in range(index+1,n):
                if properties[index][0]>properties[index2][0] and properties[index][1]>properties[index2][1]:
                    ans += 1
        return ans
                
'''
