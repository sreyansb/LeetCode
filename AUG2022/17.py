#attempt1:
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        char_to_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            newword = ""
            for char in word:
                newword += char_to_morse[ord(char)-ord('a')]
            s.add(newword)
        return len(s)
        
