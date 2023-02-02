#attempt1:
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        bigger_len = len(str1)
        smaller_len = len(str2)
        index = len(str2)-1
        while(index >= 0):
            if bigger_len%(index+1):
                index -= 1
                continue
            bigger_divisor = bigger_len//(index+1)
            smaller_divisor = smaller_len//(index+1)
            if str1 == (str2[:index+1])*bigger_divisor and str2 == (str2[:index+1])*smaller_divisor:
                return str2[:index+1]
            index -= 1
        return ""
