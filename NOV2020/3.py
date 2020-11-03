#attempt2: 99.15%
class Solution:
    def maxPower(self, s: str) -> int:
        power=1
        chara=s[0]
        curlen=1
        for i in s[1:]:
            if i==chara:
                curlen+=1
            else:
                power=max(power,curlen)
                curlen=1
                chara=i
        return max(power,curlen)
        
#attempt1: 55%
"""
class Solution:
    def maxPower(self, s: str) -> int:
        power=1
        st=[s[0]]
        for i in s[1:]:
            if not(st) or st[-1]==i:
                st.append(i)
            else:
                power=max(power,len(st))
                st=[i]
        return max(power,len(st))
        
"""
