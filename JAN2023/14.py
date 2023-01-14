#attempt2:
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {}
        for index, char1 in enumerate(s1):
            char2 = s2[index]
            if char1 not in graph:
                graph[char1] = set()
            if char2 not in graph:
                graph[char2] = set()
            graph[char1].add(char2)
            graph[char2].add(char1)
        
        connectedComponents = []

        def findConnectedComponents(currentVertex, visited):
            for equivalent in graph[currentVertex]:
                if equivalent in visited:
                    continue
                visited.append(equivalent)
                findConnectedComponents(equivalent, visited)
        
        allVisited = []
        for char in graph:
            if char not in allVisited:
                visited = [char]
                findConnectedComponents(char, visited)
                allVisited += visited
                connectedComponents.append(visited)
            #print(char, connectedComponents)
        
        smallestEquivalent = {}
        for component in connectedComponents:
            minChar = min(component)
            for char in component:
                smallestEquivalent[char] = minChar
        
        finalStr = list(baseStr)
        for index, char in enumerate(baseStr):
            if char in smallestEquivalent:
                finalStr[index] = smallestEquivalent[char]
        return "".join(finalStr)

#attempt1: WA because the graph wasn't nicely created
'''
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {}
        for index, char1 in enumerate(s1):
            char2 = s2[index]
            if char1 not in graph:
                graph[char1] = set()
            if char2 not in graph:
                graph[char2] = set()
            graph[char1].add(char2)
            graph[char2].add(char1)
        print(graph)
        smallestEquivalent = {}
        
        @lru_cache(None)
        def findAns(character, parent='z'):
            if character in smallestEquivalent:
                return character
            smallestEquivalent[character] = min(character, parent)
            for equivalent in graph[character]:
                smallestEquivalent[character] = min(smallestEquivalent[character], findAns(equivalent, smallestEquivalent[character]))
            return smallestEquivalent[character]
    
        for char in graph:
            findAns(char)
        print(smallestEquivalent)
        finalStr = list(baseStr)
        for index, char in enumerate(baseStr):
            if char in smallestEquivalent:
                finalStr[index] = smallestEquivalent[char]
        return "".join(finalStr)
'''
