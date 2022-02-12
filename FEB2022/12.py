#attempt1:
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #queue's each element will be of the form  (lastele,stack of previous words)
        wordList = set(wordList)
        queue = deque([])
        queue.append((beginWord,[beginWord]))
        beglen = len(beginWord)
        endlen = len(endWord)
        if beglen != endlen:
            return 0
        visited = {beginWord}
        while(queue):
            ele,stack = queue.popleft()
            if ele == endWord:
                return len(stack)
            for i in range(beglen):
                for charindex in range(ord('a'),ord('z')+1):
                    char = chr(charindex)
                    nextword = ele[:i] + char + ele[i+1:]
                    if nextword in wordList and nextword not in visited:
                        visited.add(nextword)
                        queue.append((nextword,stack+[nextword]))
        return 0
            
