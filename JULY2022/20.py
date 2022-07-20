#attempt1:
from bisect import bisect_left
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        di_char = {}
        for index,letter in enumerate(s):
            if letter not in di_char:
                di_char[letter] = []
            di_char[letter].append(index)
        number_of_words = 0
        for word in words:
            prev_pos = -1
            subsequence_flag = 1
            for char in word:
                if char not in di_char:
                    subsequence_flag = 0
                    break
                position_in_s = bisect_left(di_char[char],prev_pos)
                if position_in_s == len(di_char[char]):
                    subsequence_flag = 0
                    break
                prev_pos = di_char[char][position_in_s]+1
            number_of_words += subsequence_flag
        return number_of_words
                    
        
