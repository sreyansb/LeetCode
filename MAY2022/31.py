#attempt1:
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        currentnumber = 0
        n = len(s)
        if n<k:
            return False
        for bin_no in s[:k]:
            currentnumber = currentnumber*2 + int(bin_no)
        stack = set()
        mask = (1<<(k-1))-1
        #print(mask)
        for bin_no in s[k:]:
            stack.add(currentnumber)
            currentnumber &= mask
            currentnumber = currentnumber*2 + int(bin_no)
        stack.add(currentnumber)
        return len(stack) == (1<<k)
