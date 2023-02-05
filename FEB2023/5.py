#attempt1:
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []
        p_counter = Counter(p)
        s_counter = Counter(s[:p_len])
        next_index = p_len
        ans = []
        while(next_index < s_len):
            if p_counter == s_counter:
                ans.append(next_index - p_len)
            s_counter[s[next_index-p_len]] -= 1
            if s_counter[s[next_index-p_len]] == 0:
                del s_counter[s[next_index-p_len]]
            if s[next_index] not in s_counter:
                s_counter[s[next_index]] = 0
            s_counter[s[next_index]] += 1
            next_index += 1
        if s_counter == p_counter:
            ans.append(next_index - p_len)
        return ans



        
