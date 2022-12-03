#attempt1:
class Solution:
    def frequencySort(self, s: str) -> str:
        counter_characters = Counter(s)
        a = sorted(counter_characters, key=lambda x: -counter_characters[x])
        return "".join([character*counter_characters[character] for character in a])

        
