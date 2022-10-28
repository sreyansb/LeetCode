#attempt1:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in di:
                di[sorted_string] = []
            di[sorted_string].append(string)
        ans = []
        return [di[key] for key in di]
        
