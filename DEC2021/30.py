#attempt2: TOOK HELP
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k&1==0:
            return -1
        notimes = 0
        prev = -1
        visited_rems = set()
        while(prev!=0 and prev not in visited_rems):
            visited_rems.add(prev)
            notimes += 1
            if prev==-1:
                prev = 0
            prev = (prev*10 + 1)%k
        return notimes if prev==0 else -1
            
            
            
        

#attempt1: brute force approach : works in Python
