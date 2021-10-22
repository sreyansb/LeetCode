#attempt1:
class Solution:
    def frequencySort(self, s: str) -> str:
        map_char_to_freq = {}
        for i in s:
            if i not in map_char_to_freq:
                map_char_to_freq[i] = 0
            map_char_to_freq[i] += 1
        final = sorted(map_char_to_freq,key=lambda x :-map_char_to_freq[x])
        finals = ""
        for i in final:
            finals += i*map_char_to_freq[i]
        return finals
                
        