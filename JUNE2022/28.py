#attempt2:
class Solution:
    def minDeletions(self, s: str) -> int:
        char_to_count_map = {}
        for char in s:
            if char not in char_to_count_map:
                char_to_count_map[char] = 0
            char_to_count_map[char] += 1
        count_to_char_map = {}
        maxcount = 0
        for char in char_to_count_map:
            count = char_to_count_map[char]
            if count not in count_to_char_map:
                count_to_char_map[count] = 0
            count_to_char_map[count] += 1
            maxcount = max(maxcount,count)
        ans = 0
        for i in range(maxcount,0,-1):
            if i not in count_to_char_map:
                continue
            if count_to_char_map[i] > 1:
                ans += count_to_char_map[i] - 1
                if i-1 not in count_to_char_map:
                    count_to_char_map[i-1] = 0
                count_to_char_map[i-1] += count_to_char_map[i] - 1
        return ans
            
        

#attempt1: WA
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        char_to_count_map = {}
        for char in s:
            if char not in char_to_count_map:
                char_to_count_map[char] = 0
            char_to_count_map[char] += 1
        count_to_char_map = {}
        maxcount = 0
        for char in char_to_count_map:
            count = char_to_count_map[char]
            if count not in count_to_char_map:
                count_to_char_map[count] = 0
            count_to_char_map[count] += 1
            maxcount = max(maxcount,count)
        ans = 0
        for i in range(maxcount,0,-1):
            if count_to_char_map[i] > 1:
                ans += count_to_char_map[i] - 1
                if i-1 not in count_to_char_map:
                    count_to_char_map[i-1] = 0
                count_to_char_map[i-1] += count_to_char_map[i] - 1
        return ans
'''
