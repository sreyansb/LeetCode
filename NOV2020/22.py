#attempt2:80%
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s=set()
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            k=""
            for j in i:
                k+=morse[ord(j)-ord('a')]
            s.add(k)
        return len(s)
    
#Attempt1:55%
'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s=set()
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            k=""
            for j in i:
                k+=morse[ord(j)-97]
            s.add(k)
        return len(s)
'''
