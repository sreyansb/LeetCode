#attempt1:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        if s_len <= t_len:
            return s if Counter(s) == Counter(t) else ""
        t_counter = Counter(t)
        s_counter = Counter(s[:t_len])
        for char in "qwertyuiopasdfghjklzxcvbnm":
            if char not in s_counter:
                s_counter[char] = 0
        min_len = float('inf')
        ans = ""
        l_index,r_index = 0,t_len-1
        while(r_index < s_len and l_index <= r_index):
            is_valid = True
            for character in t_counter:
                if s_counter[character] < t_counter[character]:
                    is_valid = False
                    break
            if is_valid:
                if r_index-l_index+1 < min_len:
                    min_len = r_index-l_index+1
                    ans = s[l_index:r_index+1]
                s_counter[s[l_index]] -= 1
                l_index += 1
            else:
                r_index += 1
                if r_index < s_len:
                    s_counter[s[r_index]] += 1
        return ans
                    
        
