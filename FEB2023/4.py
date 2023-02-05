#attempt2:
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_len])
        index = s1_len
        while (index < s2_len):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[index-s1_len]] -= 1
            if s2_counter[s2[index - s1_len]] == 0:
                del s2_counter[s2[index-s1_len]]
            if s2[index] not in s2_counter:
                s2_counter[s2[index]] = 0
            s2_counter[s2[index]] += 1   
            print(s1_counter, s2_counter)   
            index += 1
        return s1_counter == s2_counter or False



#attempt1: WA because if the match is on the last index, it won't occur
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_len])
        index = s1_len
        while (index < s2_len):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[index-s1_len]] -= 1
            if s2_counter[s2[index - s1_len]] == 0:
                del s2_counter[s2[index-s1_len]]
            if s2[index] not in s2_counter:
                s2_counter[s2[index]] = 0
            s2_counter[s2[index]] += 1      
            index += 1
        return False


'''
