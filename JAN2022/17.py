#attempt1:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_to_s_map = {}
        s_to_pat_map = {}
        s = s.split(" ")
        n = len(pattern)
        if n != len(s):
            return False
        for i in range(n):
            if pattern[i] in pat_to_s_map:
                if pat_to_s_map[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in s_to_pat_map:
                    return False
                else:
                    pat_to_s_map[pattern[i]] = s[i]
                    s_to_pat_map[s[i]] = pattern[i]
        return True
        
        
